from pathlib import Path
from shl.healer.healer_memory import HealerMemory


class HealerStats:
    def __init__(self, memory_path="shl/healer/memory.json"):
        self.memory_path = Path(memory_path)
        self.memory = HealerMemory.load(memory_path)

    def _percent(self, success, fail):
        total = success + fail
        if total == 0:
            return "0 %"
        return f"{round((success / total) * 100)} %"

    def print_stats(self):
        print("\n=== SHL Healer Stats ===\n")

        # TEXT
        print("Text matching:")
        print(f"  Success: {self.memory.text_success}")
        print(f"  Fail:    {self.memory.text_fail}")
        print(f"  Accuracy: {self._percent(self.memory.text_success, self.memory.text_fail)}\n")

        # TYPE
        print("Type matching:")
        print(f"  Success: {self.memory.type_success}")
        print(f"  Fail:    {self.memory.type_fail}")
        print(f"  Accuracy: {self._percent(self.memory.type_success, self.memory.type_fail)}\n")

        # CONTEXT
        print("Context matching:")
        print(f"  Success: {self.memory.context_success}")
        print(f"  Fail:    {self.memory.context_fail}")
        print(f"  Accuracy: {self._percent(self.memory.context_success, self.memory.context_fail)}\n")

        # SELECTOR HISTORY
        print("Selector evolution history:")
        if not self.memory.selector_history:
            print("  (no changes yet)")
        else:
            for sel in self.memory.selector_history[-10:]:
                print(f"  - {sel}")

        print("\n========================\n")
