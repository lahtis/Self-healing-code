# Basic UI Integration

This example demonstrates how to integrate SHL into a simple user interface.  
The goal is to show how UI elements can retrieve localized text using the `Localizer` and update dynamically when the language changes.

This example is framework‑agnostic and works with any UI system (Tkinter, PyGame, Qt, Kivy, custom engines, etc.).

---

## Example Template (`template.json`)

```json
{
    "ui": {
        "title": "",
        "start_button": "",
        "exit_button": ""
    }
}
```

---

## Example Language File (en.json)
```json
{
    "ui": {
        "title": "My Application",
        "start_button": "Start",
        "exit_button": "Exit"
    }
}
```

---

## Loading SHL in Your UI
```python
from shl.engine import LocalizationEngine

engine = LocalizationEngine(base_language="en")
localizer = engine.localizer
```
Now you can retrieve UI text like this:
```python
title = localizer.get("ui.title")
start_label = localizer.get("ui.start_button")
exit_label = localizer.get("ui.exit_button")
```

---

## Example: Simple UI Class
Below is a minimal example of a UI component that uses SHL for its labels.
```python
class MainMenuUI:
    def __init__(self, localizer):
        self.localizer = localizer
        self.refresh_labels()

    def refresh_labels(self):
        self.title = self.localizer.get("ui.title")
        self.start_button = self.localizer.get("ui.start_button")
        self.exit_button = self.localizer.get("ui.exit_button")

    def render(self):
        print(f"[UI] {self.title}")
        print(f"[1] {self.start_button}")
        print(f"[2] {self.exit_button}")
```

---

## Using the UI
```python
ui = MainMenuUI(localizer)
ui.render()
```
### Output:
```python
[UI] My Application
[1] Start
[2] Exit
```

---

## Changing the Language at Runtime
SHL supports switching languages dynamically.
```python
fi_localizer = engine.localizer_for("fi")

ui.localizer = fi_localizer
ui.refresh_labels()
ui.render()
```
### Output:
```python
[UI] Sovellus
[1] Aloita
[2] Poistu
```

---

## Healing UI‑Related Keys
If a UI key is missing in a language file, SHL automatically adds it:
### Before (fi.json)
```json
{
    "ui": {
        "title": "Sovellus"
    }
}
```
### After Healing
```json
{
    "ui": {
        "title": "Sovellus",
        "start_button": "",
        "exit_button": ""
    }
}
```
Your UI will never crash due to missing translations.

---

## Summary
This example shows how SHL integrates with UI systems:
* retrieve UI labels using dot‑notation keys
* update UI dynamically when language changes
* rely on SHL’s self‑healing to prevent missing‑key errors
* keep UI code clean and translation‑safe

This pattern works for:
* games
* desktop apps
* mobile apps
* web UIs
* custom engines
SHL ensures your UI always has valid, predictable text — regardless of how many languages you support.

---
