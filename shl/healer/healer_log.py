from dataclasses import dataclass
from datetime import datetime


@dataclass
class HealerLogEntry:
    component_id: str
    old_key: str
    new_key: str
    reason: str
    confidence: float
    timestamp: str = datetime.now().isoformat()
