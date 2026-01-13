from dataclasses import dataclass, field

@dataclass
class UINode:
    id: str | None
    type: str
    text: str | None
    selector: str | None
    children: list = field(default_factory=list)

    def add_child(self, node):
        self.children.append(node)
