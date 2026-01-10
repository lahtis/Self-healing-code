from shl.engine import LocalizationEngine

engine = LocalizationEngine(lang_code="en")

# Create a new language (e.g., German)
engine.ensure_language("de")

print("German language files created:")
print("- locales/lang_de.json")
print("- prompts/de.json")
