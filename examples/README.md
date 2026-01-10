# Examples

This directory contains small, focused examples demonstrating how to use the **Self‑Healing Localization Layer (SHLL)** in real projects.  
Each example highlights a specific feature of the library, from basic UI text retrieval to full engine synchronization.

---

## 📄 `basic_ui.py`
Demonstrates how to retrieve localized UI text using the `LocalizationEngine`.

- Initializes the engine with a chosen language  
- Fetches UI strings using `ui_text()`  
- Automatically creates missing language files and missing keys  
- Shows how default values are used as fallbacks  

Use this example if you want to understand the simplest SHLL workflow.

---

## 📄 `basic_templates.py`
Shows how to retrieve localized **prompt templates**.

- Loads prompt templates via `template()`  
- Automatically creates missing template files  
- Copies the base template (`en.json`) when a language is missing  
- Adds missing template keys on the fly  

Useful for projects that localize AI prompts or structured text templates.

---

## 📄 `sync_languages.py`
Demonstrates how to synchronize all languages with the base language.

- Calls `engine.sync()`  
- Ensures every language contains all keys found in the base language  
- Adds missing keys without overwriting existing translations  

Use this when maintaining multiple languages across a growing project.

---

## 📄 `create_new_language.py`
Shows how to create a new language pack programmatically.

- Uses `engine.ensure_language("de")`  
- Automatically generates:  
  - `locales/lang_de.json`  
  - `prompts/de.json`  
- Ensures both UI and template files exist and contain all required keys  

Perfect for adding new languages without manual file creation.

---

## 📄 `full_engine_demo.py`
A complete demonstration of the SHLL engine in action.

- Retrieves UI text  
- Retrieves prompt templates  
- Demonstrates fallback behavior  
- Synchronizes all languages  
- Shows how SHLL maintains localization files automatically  

This is the best example to read if you want a full overview of how the system works.

---

## 📦 Summary

| Example file              | Purpose |
|---------------------------|---------|
| `basic_ui.py`             | Basic UI text localization |
| `basic_templates.py`      | Prompt template localization |
| `sync_languages.py`       | Synchronize all languages with base |
| `create_new_language.py`  | Create a new language pack |
| `full_engine_demo.py`     | Full demonstration of SHLL features |

---

SHLL is designed to be simple, automatic, and self‑maintaining.  
These examples should help you integrate it into any Python project quickly and confidently.
