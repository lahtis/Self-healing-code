# Installation

The Self‑Healing Localization Layer (SHLL) can be installed using pip.  
The package is currently available on TestPyPI for early testing.

---

## Installing from TestPyPI

To install the latest test release:

```bash
pip install -i https://test.pypi.org/simple/ self-healing-localization
```

To install a specific version:
```bash
pip install -i https://test.pypi.org/simple/ self-healing-localization==0.1.1
```

# Installing from PyPI (coming soon)
Once the first stable release is published, installation will be as simple as:
```bash
pip install self-healing-localization
```

Requirements
* Python 3.10 or newer
* No external dependencies
* Works on Windows, Linux, and macOS

Verifying the installation
After installation, you can verify that SHLL works by importing the engine:
```bash
from shl.engine import LocalizationEngine

engine = LocalizationEngine()
print("SHLL is installed and working.")
```
---

# Upgrading to the latest version
```bash
pip install --upgrade self-healing-localization
```
---






# 📄 **docs/quickstart.md**

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




