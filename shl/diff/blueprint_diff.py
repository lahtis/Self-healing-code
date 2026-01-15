"""
File: blueprint_diff.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Defines SHL blueprint changes: the type, reason, and old–new values of a single
component field modification for diff analysis.

Määrittelee SHL‑blueprinttien muutokset: yksittäisen komponentin kenttämuutoksen 
tyypin, syyn ja vanha–uusi‑arvot vertailua varten.
"""
from dataclasses import dataclass
from typing import Any


class ChangeType:
    ADDED = "added"
    REMOVED = "removed"
    CHANGED = "changed"


class ChangeReason:
    HEALER = "healer_update"
    MANUAL = "manual_edit"
    NORMALIZATION = "normalization"
    UNKNOWN = "unknown"


@dataclass
class BlueprintChange:
    component_id: str
    field: str
    old_value: Any
    new_value: Any
    change_type: str   # added | removed | changed
    reason: str        # healer_update | manual_edit | normalization | unknown
    confidence: float | None = None

    def __post_init__(self):
        assert self.change_type in (
            ChangeType.ADDED,
            ChangeType.REMOVED,
            ChangeType.CHANGED,
        ), f"Invalid change_type: {self.change_type}"

        assert self.reason in (
            ChangeReason.HEALER,
            ChangeReason.MANUAL,
            ChangeReason.NORMALIZATION,
            ChangeReason.UNKNOWN,
        ), f"Invalid reason: {self.reason}"

