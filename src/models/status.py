from sqlalchemy.orm import Mapped, mapped_column

from src.schemas.status_schema import StatusSchema
from src.models.base import Base


class Status(Base):
    __tablename__ = 'task_statuses'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)

    def to_read_model(self) -> StatusSchema:
        return StatusSchema(
            id=self.id,
            title=self.title
        )
