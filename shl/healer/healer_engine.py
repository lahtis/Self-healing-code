from shl.healer.healer_logger import HealerLogger
from shl.healer.healer_log import HealerLogEntry
from shl.healer.healer_memory import HealerMemory
from shl.ui_tree.ui_tree_printer import UITreePrinter


class HealerEngine:
    def __init__(self, adapter, blueprint, logger=None, memory_path="shl/healer/memory.json", debug=False):
        self.adapter = adapter
        self.blueprint = blueprint
        self.logger = logger or HealerLogger()
        self.memory_path = memory_path
        self.memory = HealerMemory.load(memory_path)
        self.debug = debug


    # -----------------------------
    #  TEXT MATCHING
    # -----------------------------
    def _find_by_text(self, component, ui_tree):
        keys = []

        if hasattr(component, "user_key") and component.user_key:
            keys.append(component.user_key)

        for k in component.text_keys.values():
            if k:
                keys.append(k)

        matches = []

        def walk(nodes):
            for node in nodes:
                if node.text:
                    if any(key.lower() in node.text.lower() for key in keys):
                        matches.append(node)
                if node.children:
                    walk(node.children)

        walk(ui_tree)
        return matches

    # -----------------------------
    #  TYPE MATCHING
    # -----------------------------
    def _find_by_type(self, component, ui_tree):
        comp_type = getattr(component, "type", None)
        if not comp_type:
            return []

        comp_type = comp_type.lower()
        matches = []

        def walk(nodes):
            for node in nodes:
                if node.type and node.type.lower() == comp_type:
                    matches.append(node)
                if node.children:
                    walk(node.children)

        walk(ui_tree)
        return matches

    # -----------------------------
    #  CONTEXT MATCHING
    # -----------------------------
    def _find_by_context(self, component, ui_tree):
        if not hasattr(component, "data_binding"):
            return []

        model = component.data_binding.get("model")
        if not model:
            return []

        matches = []

        def walk(nodes):
            for node in nodes:
                if getattr(node, "data_model", None) == model:
                    matches.append(node)
                if node.children:
                    walk(node.children)

        walk(ui_tree)
        return matches

    # -----------------------------
    #  MAIN HEALING LOGIC (ML‑assisted)
    # -----------------------------
    def repair_healer_key(self, component, ui_tree):
        old_key = getattr(component, "healer_key", None)

        # Halutessasi: debug‑tulostus koko puusta
        if self.debug:
            UITreePrinter().print_tree(ui_tree)

        # 1. kysy muistilta, mikä heuristiikka on tähän mennessä toiminut parhaiten
        methods = [
            ("text", self.memory.confidence("text")),
            ("type", self.memory.confidence("type")),
            ("context", self.memory.confidence("context")),
        ]
        methods.sort(key=lambda x: x[1], reverse=True)

        # 2. käy heuristiikat läpi järjestyksessä
        for method, weight in methods:
            finder = getattr(self, f"_find_by_{method}")
            candidates = finder(component, ui_tree)

            if len(candidates) == 1:
                new_key = candidates[0].selector

                # Muisti oppii onnistumisesta
                self.memory.record_success(method, new_key)

                # Lokitus
                self.logger.log(HealerLogEntry(
                    component_id=getattr(component, "id", "<unknown>"),
                    old_key=old_key,
                    new_key=new_key,
                    reason=f"{method}_match",
                    confidence=weight,
                ))

                self.memory.save(self.memory_path)
                
                return new_key

            else:
                # Muisti oppii, että tämä heuristiikka ei tällä kertaa riittänyt
                self.memory.record_fail(method)

        # Ei pysty korjaamaan
        self.memory.save(self.memory_path)
        return None

    def save_memory(self):
        self.memory.save(self.memory_path)
