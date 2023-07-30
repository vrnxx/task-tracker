from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    time_create: datetime
    status_id: int
    owner_id: int
    worker_id: int

    class Config:
        from_attributes = True


class TaskAddSchema(BaseModel):
    title: str
    description: Optional[str] = None
    status_id: int = Field(default=1)
    owner_id: int
    worker_id: int
