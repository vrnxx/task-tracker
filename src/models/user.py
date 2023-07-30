from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.models.dto.user import UserDto


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    def to_dto(self) -> UserDto:
        return UserDto(
            id=self.id,
            username=self.username,
            email=self.email
        )
