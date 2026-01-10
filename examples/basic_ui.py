from shl.engine import LocalizationEngine

# Initialize engine with Finnish
engine = LocalizationEngine(lang_code="fi")

# Retrieve UI text (auto-creates missing keys)
print(engine.ui_text("app_title", "My Application"))
print(engine.ui_text("welcome_message", "Welcome to the app!"))
