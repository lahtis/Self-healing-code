from shl.engine import LocalizationEngine

# Initialize engine with Swedish
engine = LocalizationEngine(lang_code="sv")

# Retrieve prompt templates (auto-creates missing keys)
summary = engine.template("summary_short", "Summarize the text:")
analysis = engine.template("analysis_prompt", "Analyze the following content:")

print(summary)
print(analysis)
