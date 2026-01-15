"""
File: healer_log.py
Author: Tuomas Lähteenmäki
Version: 0.1
License: MIT
Description: 
Data structure for a single healing log entry: records the component ID,
key change, reason, confidence score, and timestamp.

Healing‑prosessin yksittäisen lokimerkinnän tietorakenne: 
tallentaa komponentin tunnisteen, avainmuutoksen, syyn, luottamusarvon ja aikaleiman.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class HealerLogEntry:
    component_id: str
    old_key: str
    new_key: str
    reason: str
    confidence: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

