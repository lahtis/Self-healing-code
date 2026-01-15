"""
File: tkinter_adapter.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
“Tkinter UI adapter for SHL: creates Tkinter widgets from SHLComponent definitions, 
applies localized texts, and refreshes them on language change.

Tkinter‑UI‑adapteri SHL:lle: luo Tkinter‑widgetit SHLComponent‑määrittelyistä, 
asettaa lokalisoidut tekstit ja päivittää ne kielen vaihtuessa.
"""
import tkinter as tk
from shl.adapters.base import UIAdapter

class TkinterAdapter(UIAdapter):
    """
    Tkinter implementation of the SHL UI adapter.
    Creates Tkinter widgets based on SHLComponent definitions.
    """

    # -------------------------
    # Widget creation
    # -------------------------
    def create_widget(self, component):
        widget_class = component.get_framework_class("Tkinter")

        if widget_class == "Entry":
            widget = tk.Entry()
        elif widget_class == "Button":
            widget = tk.Button()
        elif widget_class == "OptionMenu":
            # Placeholder: OptionMenu requires parent + variable + options
            widget = tk.OptionMenu(None, tk.StringVar(), "")
        else:
            raise ValueError(f"Unsupported Tkinter widget class: {widget_class}")

        # Apply initial localization
        self.apply_localization(widget, component)

        return widget

    # -------------------------
    # Text application
    # -------------------------
    def set_text(self, widget, component, field_name, text):
        """
        Applies localized text to the widget.
        Tkinter has limited support for placeholders and tooltips.
        """

        # Label text (Button text)
        if field_name == "label":
            if hasattr(widget, "config"):
                widget.config(text=text)

        # Placeholder (Tkinter does not support natively)
        if field_name == "placeholder":
            # Optional: implement custom placeholder logic later
            pass

        # Tooltip (not supported natively)
        if field_name == "tooltip":
            pass

    # -------------------------
    # Refresh on language change
    # -------------------------
    def refresh_widget(self, widget, component):
        """
        Reapply all localized texts to the widget.
        """
        self.apply_localization(widget, component)


