import yaml

# --- SHL COMPONENT REGISTRY (YAML) ---
# Normaalisti tämä luettaisiin tiedostosta.
shl_schema = """
components:
  - type: "text_input"
    strategies:
      placeholder_match: 0.8
      proximity_label: 0.7

  - type: "action_button"
    strategies:
      text_match: 0.9
"""

# --- SHL HEALER ENGINE ---
class SHLHealer:
    def __init__(self, schema_yaml):
        self.registry = yaml.safe_load(schema_yaml)

    def get_strategies(self, component_type):
        """Palauttaa komponenttityypin strategiat YAML:sta."""
        for comp in self.registry["components"]:
            if comp["type"] == component_type:
                return comp["strategies"]
        return {}

    def calculate_score(self, component_type, candidate_props, target_context):
        """Laskee painotetun scoren YAML-strategioiden perusteella."""
        strategies = self.get_strategies(component_type)
        score = 0.0

        # --- Strategia 1: Tekstivastaavuus ---
        if "text" in candidate_props:
            if target_context["key_language"].lower() in candidate_props["text"].lower():
                score += strategies.get("text_match", 0)
                score += strategies.get("placeholder_match", 0)

        # --- Strategia 2: Sijainti / Proximity ---
        if candidate_props.get("near_text") == target_context.get("nearby_label"):
            score += strategies.get("proximity_label", 0)

        return score


# --- SIMULAATIO ---
print("\n--- SHL Healing prosessi käynnistetty ---\n")

# 1. Mitä käyttäjä haluaa löytää?
target = {
    "type": "text_input",
    "key_language": "Osoite",
    "nearby_label": "Toimitustiedot"
}

# 2. Mitä UI:ssa oikeasti on?
candidates = [
    {"id": "search_bar", "text": "Hae...", "near_text": "Yläpalkki"},
    {"id": "addr_new_2026", "text": "Syötä Osoite", "near_text": "Toimitustiedot"}
]

healer = SHLHealer(shl_schema)

best_match = None
best_score = 0.0

for cand in candidates:
    score = healer.calculate_score(target["type"], cand, target)
    print(f"Elementti {cand['id']}: Score {score:.2f}")

    if score > best_score:
        best_score = score
        best_match = cand

# --- Healing-päätös ---
threshold = 0.75

if best_score >= threshold:
    print(f"\n>> LÖYTYI! Paras vastaavuus: {best_match['id']}")
    print(f">> Korjataan lokaattori tähän uuteen arvoon.")
else:
    print("\n>> Ei riittävää vastaavuutta. Healing epäonnistui.")
