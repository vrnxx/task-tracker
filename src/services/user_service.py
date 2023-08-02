from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.models.dto.user import UserDto
from src.schemas.user_schema import UserAddSchema


class UserService:
    def __init__(self, user_dao: AbstractDAO):
        self.user_dao: AbstractDAO = user_dao()

    async def get_user_by_id(self, user_id: int) -> UserDto:
        user = await self.user_dao.find_one(user_id)
        return user

    async def get_all_users(self) -> list[UserDto]:
        users = await self.user_dao.find_all()
        return users

    async def add_user(self, user: UserAddSchema) -> UserDto:
        new_user = await self.user_dao.add_one(user.model_dump())
        return new_user

    async def update_user(self, user_id: int, new_data: UserAddSchema) -> UserDto:
        updated_user = await self.user_dao.update_one(user_id, new_data.model_dump())
        return updated_user

    async def delete_user(self, user_id: int) -> UserDto:
        deleted_user = await self.user_dao.delete_one(user_id)
        return deleted_user
