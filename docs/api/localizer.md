# Localizer API

The `Localizer` class provides the public interface for retrieving localized text in the Self‑Healing Localization Layer (SHL).  
It is designed to be simple, predictable, and safe to use in any application.

The `LocalizationEngine` creates and manages the `Localizer` instance automatically.

---

## Class: Localizer

```python
class Localizer:
    def __init__(self, engine, language: str):
        ...
 ```

---

## Parameters
| Name     | Type                | Description                                           |
|----------|---------------------|-------------------------------------------------------|
| engine   | LocalizationEngine  | Reference to the engine that manages all localization data. |
| language | str                 | The language code this localizer retrieves text for. |


---

## Purpose
The `Localizer` is responsible for:
* retrieving translated strings
* resolving nested keys using dot‑notation
* falling back to the base language when needed
* ensuring safe access (no crashes on missing keys)
It does not modify files — all write operations are handled by the engine.

---

## Methods

### get()

```python
localizer.get(key: str) -> str
```
Retrieves a localized string using a dot‑notation key.

### Example
```python
text = engine.localizer.get("menu.start")
```
### Behavior
* returns the translation for the selected language
* if missing, falls back to the base language
* if still missing, returns the key itself (safe fallback)

---

### exists()
```python
localizer.exists(key: str) -> bool
```
Checks whether a key exists in the current language or fallback language.

### Example
```python
if localizer.exists("errors.network"):
    ...
```

---

## #available_languages()
```python
localizer.available_languages() -> list[str]
```
Returns a list of all languages loaded by the engine.

Equivalent to:
```python
engine.get_languages()
```

---

## Key Format
The `Localizer` uses dot‑notation to access nested JSON keys.

### Example JSON
```json
{
    "menu": {
        "start": "Start",
        "exit": "Exit"
    }
}
```
## Accessing keys
```python
localizer.get("menu.start")
localizer.get("menu.exit")
```
---

## Fallback Logic
The fallback chain is:
* 1. Current language
* 2. Base language (default: "en")
* 3. Return key itself
This ensures that applications never crash due to missing translations.

---

### Usage Example
```python
from shl.engine import LocalizationEngine

engine = LocalizationEngine(base_language="en")

# Retrieve text in the base language
print(engine.localizer.get("menu.start"))

# Retrieve text in another language
fi = engine.get_language_data("fi")
fi_localizer = engine.localizer_for("fi")

print(fi_localizer.get("menu.start"))
```

---

## Error Handling
The Localizer is designed to be safe:
* No KeyError is ever raised
* Missing keys return the key name
* Invalid key formats return the key name
* Fallbacks ensure predictable behavior
  
---

## Summary
The Localizer provides:
* simple access to translated strings
* safe fallback behavior
* dot‑notation key resolution
* integration with the LocalizationEngine
It is the primary interface applications use to retrieve localized text in SHL.
