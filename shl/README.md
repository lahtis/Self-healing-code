# SHL — Core Concepts

## What SHL is (and is not)

### SHL is
- **Self‑healing localization layer**  
  A system that automatically repairs UI localization when the UI changes.
- **A layered architecture**, not an application  
  SHL sits between registry → middleman → healer → adapters.
- **Deterministic and rule‑based**  
  No machine learning, no guessing, no black boxes.
- **Explainable and traceable**  
  Every decision can be inspected and justified.
- **A bridge between UI structure and localization**  
  It connects blueprint, UCR, UI tree and adapters.

### SHL is NOT
- ❌ a translation engine  
- ❌ a language model  
- ❌ a heuristic guesser  
- ❌ a UI framework  
- ❌ an automatic UI builder  
- ❌ magic  
- ❌ a black box  

SHL is a **transparent, deterministic analysis system**.

---

## Diff vs Patch vs Heal

### Diff
- Compares two things  
- Does not modify data  
- Produces a report: *“Here is the difference.”*

### Patch
- Applies a change  
- Produces a new version of the data  
- Example: healer modifies a blueprint

### Heal
- The decision‑making process  
- Chooses the correct patch  
- Produces a resolution and scores

### Summary

| Operation | Purpose | Modifies Data |
|----------|----------|----------------|
| Diff | Detect differences | No |
| Patch | Apply changes | Yes |
| Heal | Decide + patch | Yes |

---

## Score, Confidence and Resolution

### Resolution
The final decision made by the healer.  
Examples:
- “Replace text_key X → Y”
- “Remove this node”
- “No change”

### Score
A value between 0–1 describing **how well a proposed resolution fits the context**.

### Confidence
A value describing **how strongly the healer prefers this resolution over alternatives**.

---

## score ≠ truth
Score does **not** indicate correctness.  
SHL does not know what the UI *should* be — only what fits best given the available data.

---

## score ≠ probability
Score is **not** a probability.  
It does not mean:
- “95% chance this is correct”
- “This is likely to happen”

SHL is not a statistical model.

---

## score = contextual fit index
This is the key principle.

**Score measures how well a resolution fits the current context**, which may include:
- blueprint  
- UCR  
- UI tree  
- component metadata  
- framework constraints  
- heuristics  
- previous changes  

Score is **relative**, not absolute.

---

## Experimental status

SHL is currently:
- **experimental**
- **actively evolving**
- **not production‑ready**
- **a research‑driven system**
- **a platform for exploring new localization and UI‑healing concepts**

This status helps set expectations for contributors and users.
