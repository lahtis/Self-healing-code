"""
File: qt_ui_tree_builder.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Builds an SHL‑compatible UI tree from a Qt widget hierarchy and constructs the UINode structure from Qt components.
Rakentaa Qt‑widget‑hierarkiasta SHL‑yhteensopivan UI‑puun ja muodostaa UINode‑rakenteen Qt‑komponenteista.
"""
from shl.ui_tree.ui_node import UINode
from shl.ui_tree.ui_tree_builder import UITreeBuilder

class QtUITreeBuilder(UITreeBuilder):
    def __init__(self, root_widget):
        self.root = root_widget

    def build_tree(self):
        return [self._build_node(self.root)]

    def _build_node(self, widget):
        node = UINode(
            id=widget.objectName(),
            type=widget.__class__.__name__,
            text=getattr(widget, "text", lambda: None)(),
            selector=f"objectName={widget.objectName()}"
        )

        for child in widget.children():
            if child.__class__.__name__.startswith("Q"):
                node.add_child(self._build_node(child))

        return node

