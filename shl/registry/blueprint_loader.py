import json
from pathlib import Path
from shl.ui.components.SHLComponent import SHLComponent


def load_blueprint(path: str | Path):
    """
    Loads a UI Blueprint JSON file and returns a list of SHLComponent objects.
    The blueprint describes:
      - component type
      - healer_key
      - user_key
      - framework_map
      - text_keys (optional)
      - data_binding (optional)
    """

    path = Path(path)

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    components = []

    for comp_id, comp_data in data.get("components", {}).items():
        component = SHLComponent(comp_id)

        # Attach text keys (label, placeholder, tooltip…)
        if "text_keys" in comp_data:
            for key, value in comp_data["text_keys"].items():
                component.text_keys[key] = value

        # Attach healer key (used for self-healing)
        if "healer_key" in comp_data:
            component.healer_key = comp_data["healer_key"]

        # Attach user key (human-readable meaning)
        if "user_key" in comp_data:
            component.user_key = comp_data["user_key"]

        # Attach framework mapping (Flet, PyQt, Playwright…)
        if "framework_map" in comp_data:
            for fw, fw_data in comp_data["framework_map"].items():
                component.framework_map[fw] = fw_data

        # Attach data binding (optional)
        if "data_binding" in comp_data:
            component.data_binding = comp_data["data_binding"]

        components.append(component)

    return components
