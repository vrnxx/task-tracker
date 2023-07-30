from sqlalchemy import select, insert, update, delete
from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.db.db import async_session_maker
from src.models.user import User


class UserDAO(AbstractDAO):
    model = User

    async def add_one(self, user_data: dict) -> User:
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**user_data).
                    returning(self.model))
            new_user = await session.scalar(stmt)
            await session.commit()

            return new_user

    async def find_one(self, user_id: int) -> User:
        async with async_session_maker() as session:
            stmt = (select(self.model).
                    where(self.model.id == user_id))
            user = await session.scalar(stmt)
            return user

    async def find_all(self) -> list[User]:
        async with async_session_maker() as session:
            stmt = select(self.model)
            users = await session.scalars(stmt)
            return users

    async def update_one(self, *args, **kwargs):
        async with async_session_maker() as session:
            print('update_one')
            return True

    async def delete_one(self, *args, **kwargs):
        async with async_session_maker() as session:
            print('delete_one')
            return True
