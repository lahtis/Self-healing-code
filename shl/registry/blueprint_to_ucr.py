import json
from pathlib import Path


def blueprint_to_ucr(blueprint_path: str | Path, output_path: str | Path):
    """
    Converts a UI Blueprint JSON file into a UCR JSON file.
    - Blueprint: human-friendly, semantic, purpose-driven
    - UCR: strict, SHL-internal registry format
    """

    blueprint_path = Path(blueprint_path)
    output_path = Path(output_path)

    with open(blueprint_path, "r", encoding="utf-8") as f:
        blueprint = json.load(f)

    ucr = {
        "$schema_version": "0.1",
        "components": {}
    }

    for comp_id, comp_data in blueprint.get("components", {}).items():
        ucr_entry = {
            "type": comp_data.get("type"),
            "text_keys": comp_data.get("text_keys", {}),
            "framework_map": comp_data.get("framework_map", {})
        }

        # Optional fields
        if "data_binding" in comp_data:
            ucr_entry["data_binding"] = comp_data["data_binding"]

        # Healer key becomes part of framework_map["Healer"]
        if "healer_key" in comp_data:
            ucr_entry.setdefault("framework_map", {})
            ucr_entry["framework_map"]["Healer"] = {
                "selector": comp_data["healer_key"]
            }

        # User key becomes metadata for Middleman / LanguageManager
        if "user_key" in comp_data:
            ucr_entry["user_key"] = comp_data["user_key"]

        ucr["components"][comp_id] = ucr_entry

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ucr, f, indent=2, ensure_ascii=False)

    return output_path
