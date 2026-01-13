import yaml

# --- YAML-SANASTO ---
shl_schema = """
components:
  - type: "action_button"
    strategies:
      text_match: 0.9
    inflection: "imperative"

  - type: "text_input"
    strategies:
      placeholder_match: 0.8
      proximity_label: 0.7
    inflection: "partitive"

  - type: "label"
    strategies: {}
    inflection: "nominative"
"""

# --- KIELIOPPIMOOTTORI ---
class SHLLocalizer:
    def __init__(self, schema_yaml):
        self.registry = yaml.safe_load(schema_yaml)

    def get_inflection(self, component_type):
        """Hakee komponentin taivutusmuodon YAML-sanastosta."""
        for comp in self.registry["components"]:
            if comp["type"] == component_type:
                return comp.get("inflection", "nominative")
        return "nominative"

    def suggest_localization(self, component_type, base_word):
        """Valitsee oikean taivutusmuodon ja generoi lokalisaatiotekstin."""
        inflection = self.get_inflection(component_type)
        word = base_word.lower()

        if inflection == "imperative":
            return f"Tallenna {word}"

        if inflection == "partitive":
            return f"Syötä {word}..."

        if inflection == "nominative":
            return base_word.capitalize()

        return base_word.capitalize()  # fallback


# --- DEMO ---
localizer = SHLLocalizer(shl_schema)

print(localizer.suggest_localization("action_button", "Osoite"))
# → "Tallenna osoite"

print(localizer.suggest_localization("text_input", "Osoite"))
# → "Syötä osoite..."

print(localizer.suggest_localization("label", "Osoite"))
# → "Osoite"
