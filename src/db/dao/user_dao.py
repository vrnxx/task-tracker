from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.dao.base_dao import BaseDAO
from src.models.dto.user import UserDto
from src.models.user import User
from src.utils.exceptions.exc_mappers import user_exception_mapper


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    @user_exception_mapper
    async def add_one(self, user_data: dict) -> UserDto:
        stmt = insert(self.model).values(**user_data).returning(self.model)
        added_user = await self.session.scalar(stmt)
        return added_user.to_dto()

    async def find_all(self) -> list[UserDto]:
        users = await self._get_all()
        return [user.to_dto() for user in users]

    @user_exception_mapper
    async def find_one_by_id(self, user_id: int) -> UserDto:
        stmt = select(self.model).where(self.model.id == user_id)
        user = await self.session.scalar(stmt)
        return user.to_dto()

    @user_exception_mapper
    async def update_one(self, user_id: int, new_user_data: dict) -> UserDto:
        stmt = (
            update(self.model)
            .where(self.model.id == user_id)
            .values(**new_user_data)
            .returning(self.model)
        )
        updated_user = await self.session.scalar(stmt)
        return updated_user.to_dto()

    @user_exception_mapper
    async def delete_one_by_id(self, user_id: int) -> UserDto:
        stmt = (
            delete(self.model)
            .where(self.model.id == user_id)
            .returning(self.model)
        )
        deleted_user = await self.session.scalar(stmt)
        return deleted_user.to_dto()
