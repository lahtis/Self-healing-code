"""
File: healer_memory_old.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Early SHL prototype where UI tree construction was still part of the healer layer. 
Implements conversion of a Qt widget hierarchy into UINode structures
before this logic was moved into the dedicated qt_ui_tree_builder module. Preserved for historical reference.

Varhainen SHL‑prototyyppi, jossa UI‑puun rakentaminen oli vielä osa healer‑kerrosta. 
Toteuttaa Qt‑widget‑hierarkian muunnoksen UINode‑rakenteeksi ennen kuin tämä logiikka siirrettiin 
omaan qt_ui_tree_builder‑moduuliinsa. Säilytetään historiallisista syistä
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

