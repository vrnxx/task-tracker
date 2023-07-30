from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.schemas.user_schema import UserAddSchema, UserSchema
from src.models.user import User


class UserService:
    def __init__(self, user_dao: AbstractDAO):
        self.user_dao: AbstractDAO = user_dao()

    async def get_user_by_id(self, user_id: int) -> User:
        user = await self.user_dao.find_one(user_id)
        return user

    async def get_all_users(self) -> list[User]:
        users = await self.user_dao.find_all()
        return users

    async def add_user(self, user: UserAddSchema) -> User:
        new_user = await self.user_dao.add_one(user.model_dump())
        return new_user
