from dataclasses import dataclass, field
from datetime import datetime, timedelta

@dataclass
class ServerInfo:
    guild: int
    channel: int
    date: datetime = field(default_factory=lambda: datetime.now() + timedelta(days=1))

