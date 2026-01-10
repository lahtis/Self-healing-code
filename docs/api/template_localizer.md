# TemplateLocalizer API

The `TemplateLocalizer` is responsible for managing the base localization template (`template.json`) and ensuring that all language files stay structurally aligned with it.  
It is a core component of SHL’s self‑healing architecture.

This document describes the public API of the `TemplateLocalizer` class.

---

## Class: TemplateLocalizer

```python
class TemplateLocalizer:
    def __init__(self, engine):
        ...
```

## Parameters
| Name   | Type                | Description                                           |
|--------|---------------------|-------------------------------------------------------|
| engine | LocalizationEngine  | Reference to the engine that manages all localization data. |


---

## Purpose
The TemplateLocalizer handles:
* loading the base template
* validating language files against the template
* generating new language files
* adding missing keys
* ensuring structural consistency across all languages
It does not translate text — it only manages structure.

---

## Methods
### load_template()
```python
template_localizer.load_template() -> dict
```
Loads and returns the contents of `template.json`.

Used internally by the engine, but available for tools and editors.

---

### generate_language_file()
```python
template_localizer.generate_language_file(language: str) -> dict
```
Creates a new language file based on the template.

#### Behavior
* returns a dictionary containing the template structure
* does not overwrite existing files
* used when a language file is missing

---

### heal_language()
```python
template_localizer.heal_language(language: str, data: dict) -> dict
```
Synchronizes a language file with the template.

#### Responsibilities
* adds missing keys
* ensures correct nesting
* preserves existing translations
* returns the healed dictionary
This is the core of SHL’s self‑healing behavior.

---

### heal_all_languages()
```python
template_localizer.heal_all_languages() -> None
```
Runs the healing process for every language loaded by the engine.

Equivalent to:
```python
engine.heal()
```
---

## Template Structure
The template defines the canonical structure for all languages.

### Example (`template.json`)
```json
{
    "menu": {
        "start": "",
        "exit": ""
    },
    "errors": {
        "network": ""
    }
}
```
The template:
* defines required keys
* defines required nesting
* leaves values empty
* acts as the single source of truth

  ---

### Example Usage
```python
from shl.engine import LocalizationEngine

engine = LocalizationEngine()
template = engine.template_localizer.load_template()

# Generate a new language file
new_lang = engine.template_localizer.generate_language_file("sv")

# Heal an existing language
healed = engine.template_localizer.heal_language("fi", engine.get_language_data("fi"))
```
  
---

### Error Handling
#### FileNotFoundError
```python
If template.json is missing.
```
#### ValueError
If the template contains invalid JSON.

---

## Summary
The TemplateLocalizer ensures that:
* all languages follow the same structure
* missing keys are added automatically
* new languages can be generated instantly
* existing translations are preserved
* SHL remains stable and predictable
It is a foundational component of SHL’s self‑healing architecture.

---

