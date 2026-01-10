# Templates

Templates define the canonical structure for all localization files in SHL.  
They ensure that every language follows the same schema, enabling SHL’s self‑healing behavior.

This guide explains how templates work, how to modify them, and how SHL uses them to maintain consistency across all languages.

---

# 1. What Is a Template?

A template is a JSON file named `template.json` located in the `locales/` directory.

It defines:

- the required keys  
- the required nesting structure  
- the shape of all language files  
- empty values (placeholders for translations)

Example:

```json
{
    "menu": {
        "start": "",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "farewell": ""
    }
}
```
This structure becomes the “source of truth” for all languages.

---

# 2. How SHL Uses Templates
SHL loads the template at startup and uses it to:
* generate new language files
* validate existing languages
* add missing keys
* restore missing sections
* ensure structural consistency
Templates are the backbone of SHL’s self‑healing system.

---

# 3. Modifying the Template
When you add new keys or sections to template.json, SHL will automatically propagate these changes to all languages.

Example: Adding a new key
```json
{
    "messages": {
        "welcome": "",
        "farewell": "",
        "error": ""
    }
}
```

After modifying the template, run:
```python
engine.sync()
```
SHL will:
* add messages.error to every language
* preserve existing translations
* never overwrite human‑written text

---

# 4. Creating New Languages from the Template
To create a new language:
```python
engine.ensure_language("de")
```

This generates:
* `locales/lang_de.json`
* `prompts/de.json` (if prompts are used)
Both files follow the template structure exactly.

---

# 5. Healing Existing Languages
If a language file is missing keys, SHL fills them in automatically.

## Before (`fi.json`)
```json
{
    "menu": {
        "start": "Aloita"
    }
}
```
## After Healing
```json
{
    "menu": {
        "start": "Aloita",
        "exit": ""
    },
    "messages": {
        "welcome": "",
        "farewell": ""
    }
}
```
SHL:
* preserved existing translations
* added missing keys
* restored missing sections

---

# 6. Best Practices for Working with Templates
✔ Keep templates clean and minimal
Only define keys that all languages must have.

✔ Avoid putting real text in the template
Values should remain empty:

```json
"welcome": ""
```

✔ Add new keys to the template first
Never edit language files directly to add new keys.

✔ Run engine.sync() after template changes
This ensures all languages stay aligned.

✔ Use consistent naming
Prefer dot‑notation friendly structures:
```json
menu.start
menu.exit
messages.welcome
```

---

# 7. When to Update the Template
Update template.json when:
* adding new UI elements
* adding new messages or prompts
* restructuring your localization schema
* preparing for new features in your app
SHL will handle the rest.

---

# Summary
Templates are the foundation of SHL’s self‑healing system.
They ensure that:
* all languages share the same structure
* missing keys are automatically added
* new languages can be generated instantly
* existing translations are preserved
* localization remains predictable and maintainable
By keeping your template clean and consistent, SHL can manage the rest automatically.

---
