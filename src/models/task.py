from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from src.models.task_status import TaskStatus
from src.schemas.task_schema import TaskSchema


class Base(DeclarativeBase):
    ...


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    time_create: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    status_id: Mapped[int] = mapped_column(ForeignKey(TaskStatus.id))
    owner: Mapped[str] = mapped_column(nullable=True)

    status = relationship(TaskStatus)

    def to_read_model(self) -> TaskSchema:
        return TaskSchema(
            id=self.id,
            title=self.title,
            description=self.description,
            time_create=self.time_create,
            status_id=self.status_id
        )
