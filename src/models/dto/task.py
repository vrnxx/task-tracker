from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class TaskDto:
    id: int
    title: str
    time_create: datetime
    status_id: int
    owner_id: int
    worker_id: int
    description: str = field(default=None)
