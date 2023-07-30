from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.dto.status import StatusDto


class Status(Base):
    __tablename__ = 'task_statuses'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)

    def to_dto(self) -> StatusDto:
        return StatusDto(
            id=self.id,
            title=self.title
        )
