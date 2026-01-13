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
