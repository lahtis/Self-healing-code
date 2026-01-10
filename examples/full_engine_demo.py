from shl.engine import LocalizationEngine

# Full demonstration of the engine
engine = LocalizationEngine(lang_code="fi")

print("=== UI TEXT ===")
print(engine.ui_text("menu_file", "File"))
print(engine.ui_text("menu_edit", "Edit"))
print(engine.ui_text("menu_help", "Help"))

print("\n=== PROMPT TEMPLATES ===")
print(engine.template("summary_short", "Summarize the text:"))
print(engine.template("explain_prompt", "Explain the following content:"))

print("\n=== SYNC ===")
engine.sync()
print("All languages synchronized with base language.")
