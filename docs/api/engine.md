# LocalizationEngine API

## Initialization

```python
LocalizationEngine(lang_code="fi")
```

Methods

ui_text(key, default="")

Returns localized UI text.

template(key, default="")

Returns localized template text.

ensure_language(lang_code)

Creates missing language files.

sync()

Synchronizes all languages with the base language.