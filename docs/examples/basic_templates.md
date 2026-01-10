
# Basic Templates

This example demonstrates how SHL uses templates to define the structure of all localization files.  
Templates ensure that every language follows the same schema, enabling SHL’s self‑healing behavior.

A template is stored in `template.json` inside the `locales/` directory.  
It defines the required keys and structure, but leaves values empty.

---

## Template Example (`template.json`)

```json
{
    "menu": {
        "start": "",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "goodbye": ""
    }
}
```
This template defines:
* two top‑level sections (`menu`, `messages`)
* four required keys (`start`, `exit`, `welcome`, `goodbye`)
* empty values (to be filled by translators)
Every language file must follow this structure.

---

## Using Templates in Code
The LocalizationEngine automatically loads the template and uses it to:
* validate language files
* generate missing languages
* add missing keys
* ensure consistent structure

### Example: Accessing the Template
```Python
from shl.engine import LocalizationEngine

engine = LocalizationEngine()

template = engine.template_localizer.load_template()
print(template)
```
This prints the parsed contents of `template.json`.

---

## Generating a New Language File
If you want to create a new language (e.g., Swedish), SHL can generate it directly from the template:
```Python
sv_data = engine.template_localizer.generate_language_file("sv")
print(sv_data)
```
### Output:
```json
{
    "menu": {
        "start": "",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "goodbye": ""
    }
}
```
This file can then be saved and translated.

---

## Healing an Existing Language File
If a language file is missing keys, SHL fills them in automatically.

### Example: Before Healing (fi.json)
```json
{
    "menu": {
        "start": "Aloita"
    }
}
```
### Healing the File
```Python
fi_data = engine.get_language_data("fi")
healed = engine.template_localizer.heal_language("fi", fi_data)
print(healed)
```
### After Healing
```json
{
    "menu": {
        "start": "Aloita",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "goodbye": ""
    }
}
```

---

## 📄 **docs/examples/basic_templates.md**

```markdown
# Example: Basic Templates

```python
engine.template("summary_short", "Summarize the text:")
```
SHL:
* preserved existing translations
* added missing keys
* restored missing sections
* aligned structure with the template

---

## Using Templates for Prompt‑Based Workflows (Optional)
If you are using SHL together with AI‑assisted translation tools, you can also use template keys as prompts.

### Example:
```python
engine.template("summary_short", "Summarize the text:")
```
This is not part of the core SHL engine, but demonstrates how template keys can be used in custom workflows.

---
## Summary
Templates are the foundation of SHL’s self‑healing system.

They ensure that:
* all languages share the same structure
* missing keys are automatically added
* new languages can be generated instantly
* existing translations are never overwritten
This example shows how templates work in practice and how they keep localization predictable and maintainable.



