from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from src.schemas.status_schema import StatusSchema


class Base(DeclarativeBase):
    ...


class Status(Base):
    __tablename__ = 'task_statuses'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(nullable=False, index=True)

    def to_read_model(self) -> StatusSchema:
        return StatusSchema(
            id=self.id,
            title=self.title
        )
