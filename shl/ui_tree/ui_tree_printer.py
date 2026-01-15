"""
File: ui_tree_printer.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
UI tree printing utility: provides methods for pretty‑printing a UINode‑based UI tree with indentation. Used for debugging, 
snapshot inspection, and understanding UI structure across middleman and healer layers

UI‑puun tulostustyökalu: tarjoaa metodit UINode‑pohjaisen käyttöliittymäpuun kauniiseen, sisennettyyn tulostamiseen. 
Käytetään debuggaamiseen, snapshot‑tarkasteluun ja UI‑puun rakenteen hahmottamiseen middleman‑ ja healer‑kerroksissa.
"""
from shl.ui_tree.ui_node import UINode


class UITreePrinter:
    def print_tree(self, nodes, indent=0):
        """
        Pretty-prints a list of UINode objects as a visual tree.
        """

        for node in nodes:
            self._print_node(node, indent)

    def _print_node(self, node: UINode, indent: int):
        prefix = "  " * indent
        print(f"{prefix}- {node.type}", end="")

        if node.id:
            print(f"  id='{node.id}'", end="")

        if node.text:
            print(f"  text='{node.text}'", end="")

        if node.selector:
            print(f"  selector='{node.selector}'", end="")

        print()  # newline

        for child in node.children:
            self._print_node(child, indent + 1)

