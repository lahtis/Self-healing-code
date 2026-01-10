from shl.engine import LocalizationEngine

# Sync all languages with the base language
engine = LocalizationEngine(lang_code="en")

print("Synchronizing all languages with base language...")
engine.sync()
print("Done.")
