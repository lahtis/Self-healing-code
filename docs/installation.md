# Installation

## Clone the Repository

```bash
git clone https://github.com/lahtis/Self-healing-localization
```

Requirements
Python 3.8 or newer

No external dependencies

Importing the Engine
```bash
from shl.engine import LocalizationEngine
```


---

# 📄 **docs/quickstart.md**

```markdown
# Quick Start

This guide shows how to get started with SHLL in under a minute.

## 1. Initialize the Engine

```python
from shl.engine import LocalizationEngine
engine = LocalizationEngine(lang_code="fi")
```

2. Retrieve UI Text
```python
title = engine.ui_text("app_title", "My Application")
```

If the key or file is missing, SHLL creates it automatically.

3. Retrieve Prompt Templates
```python
summary = engine.template("summary_short", "Summarize the text:")
```
Missing template files and keys are also created automatically.


---

# 📁 **docs/concepts/**

## 📄 **docs/concepts/overview.md**

```markdown
# Core Concepts

SHLL is built around three ideas:

1. **Self‑healing localization**  
2. **Unified engine for UI and templates**  
3. **Automatic synchronization**

The system ensures that your localization files are always complete, without manual editing.


