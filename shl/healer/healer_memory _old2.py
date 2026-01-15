"""
File: healer_memory _old2.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Early SHL memory prototype: a simple counter tracking text, type, and context
successes/failures and the history of selected selectors. Served as the foundation
for the current heuristic and learning‑based healer memory system. Preserved for historical reference.

SHL:n varhainen muistiprototyyppi: yksinkertainen laskuri, joka tallentaa tekstin,
tyypin ja kontekstin onnistumis‑ ja epäonnistumismäärät sekä valittujen selectorien historian.
Toimi pohjana nykyiselle heuristiikka‑ ja oppimispohjaiselle healer‑muistijärjestelmälle. 
Säilytetään historiallisista syistä.
"""

from dataclasses import dataclass, field

@dataclass
class HealerMemory:
    text_success: int = 0
    text_fail: int = 0

    type_success: int = 0
    type_fail: int = 0

    context_success: int = 0
    context_fail: int = 0

    selector_history: list = field(default_factory=list)

    def record_success(self, method: str, selector: str | None):
        attr = f"{method}_success"
        setattr(self, attr, getattr(self, attr) + 1)
        if selector:
            self.selector_history.append(selector)

    def record_fail(self, method: str):
        attr = f"{method}_fail"
        setattr(self, attr, getattr(self, attr) + 1)

    def confidence(self, method: str) -> float:
        s = getattr(self, f"{method}_success")
        f = getattr(self, f"{method}_fail")
        total = s + f
        # 0.5 = neutraali alkuarvo
        return s / total if total > 0 else 0.5

