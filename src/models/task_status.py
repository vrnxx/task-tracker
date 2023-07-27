from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.schemas.task_status_schema import TaskStatusSchema


class Base(DeclarativeBase):
    ...


class TaskStatus(Base):
    __tablename__ = 'task_statuses'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)

    def to_read_model(self) -> TaskStatusSchema:
        return TaskStatusSchema(
            id=self.id,
            title=self.title
        )
