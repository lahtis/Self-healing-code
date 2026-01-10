# UI Texts

This guide explains how to organize and retrieve UI‑related text using the Self‑Healing Localization Layer (SHL).  
UI texts are one of the most common use cases for localization, and SHL provides a clean, predictable, and safe workflow for managing them.

---

# 1. Organizing UI Texts in the Template

UI texts should be grouped under a dedicated section in `template.json`, typically named `ui`.

Example:

```json
{
    "ui": {
        "title": "",
        "start_button": "",
        "exit_button": "",
        "settings_button": ""
    }
}
```
This structure becomes the source of truth for all languages.

---

# 2. Example Language File
A language file (e.g., `en.json`) mirrors the template:
```json
{
    "ui": {
        "title": "My Application",
        "start_button": "Start",
        "exit_button": "Exit",
        "settings_button": "Settings"
    }
}
```
SHL ensures all languages follow this structure.

---

# 3. Retrieving UI Texts in Code
UI components retrieve text using the `Localizer:`
```python
localizer = engine.localizer

title = localizer.get("ui.title")
start_label = localizer.get("ui.start_button")
exit_label = localizer.get("ui.exit_button")
```

This works with any UI framework:
* PyGame
* Kivy
* Qt
* Tkinter
* Custom engines
* Web UIs (via Python backend)

---

# 4. Example: UI Component Class
```python
class MainMenuUI:
    def __init__(self, localizer):
        self.localizer = localizer
        self.refresh()

    def refresh(self):
        self.title = self.localizer.get("ui.title")
        self.start = self.localizer.get("ui.start_button")
        self.exit = self.localizer.get("ui.exit_button")

    def render(self):
        print(f"=== {self.title} ===")
        print(f"[1] {self.start}")
        print(f"[2] {self.exit}")
```

---

# 5. Updating UI When Language Changes
Switching languages is simple:
```python
fi_localizer = engine.localizer_for("fi")

ui.localizer = fi_localizer
ui.refresh()
ui.render()
```
The UI updates instantly without restarting the engine.

---

# 6. Handling Missing UI Keys
If a UI key is missing in a language file, SHL automatically heals it.

## Before (`fi.json`)
```json
{
    "ui": {
        "title": "Sovellus"
    }
}
```
## After Healing
```json
{
    "ui": {
        "title": "Sovellus",
        "start_button": "",
        "exit_button": "",
        "settings_button": ""
    }
}
```
Your UI will never crash due to missing translations.

---
# 7. Best Practices for UI Texts

✔ Group UI texts under ui
Keeps the structure clean and predictable.

✔ Use descriptive, consistent key names
Examples:

* `ui.start_button`
* `ui.exit_button`
* `ui.settings.title`

✔ Avoid embedding formatting in translations
## Prefer:
```json
"welcome": "Welcome!"
```
## Not:
```json
"welcome": "<b>Welcome!</b>"
```
✔ Keep UI logic separate from localization logic
UI components should only call `localizer.get(`).

✔ Run `engine.sync()` after modifying the template
Ensures all languages stay aligned.

---

# Summary
UI texts are one of the most important parts of localization.
SHL makes them:
* easy to organize
* safe to retrieve
* automatically healed
* consistent across languages
* simple to update at runtime
By structuring UI texts cleanly and using SHL’s self‑healing features, your UI remains stable, predictable, and fully multilingual.
