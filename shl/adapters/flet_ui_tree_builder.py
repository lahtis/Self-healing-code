"""
File: flet_ui_tree_builder.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Builds a Flet‑based UI tree from SHL components and constructs the widget hierarchy inside the adapter.
Rakentaa SHL‑komponenttien pohjalta Flet‑pohjaisen UI‑puun ja huolehtii widget‑hierarkian muodostamisesta adapterin sisällä.
"""
from shl.ui_tree.ui_node import UINode
from shl.ui_tree.ui_tree_builder import UITreeBuilder

class FletUITreeBuilder(UITreeBuilder):
    def __init__(self, page):
        self.page = page

    def build_tree(self):
        nodes = []
        for control in self.page.controls:
            nodes.append(self._build_node(control))
        return nodes

    def _build_node(self, control):
        node = UINode(
            id=getattr(control, "id", None),
            type=control.__class__.__name__,
            text=getattr(control, "value", None) or getattr(control, "text", None),
            selector=f"id={control.id}" if getattr(control, "id", None) else None
        )

        for child in getattr(control, "controls", []):
            node.add_child(self._build_node(child))

        return node

