from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError

from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.db.db import async_session_maker
from src.models.dto.user import UserDto
from src.models.user import User
from src.utils.exceptions import UserEmailNotUnique, UserNotFoundError


class UserDAO(AbstractDAO):
    """
    Class for management of User-model in the database.

    Implements AbstractDAO methods.
    Returned values from methods are UserDto instances.
    """
    model = User

    async def add_one(self, user_data: dict) -> UserDto:
        """
        Add a new user to the database.

        Raise UserEmailNotUnique if entered email is
        already in the database.

        :except : UserEmailNotUnique
        :param user_data: data for new user.
        :return: UserDto instance
        """
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**user_data).
                    returning(self.model))
            try:
                new_user = await session.scalar(stmt)
                await session.commit()
            except IntegrityError:
                raise UserEmailNotUnique()

            return new_user.to_dto()

    async def find_one(self, user_id: int) -> UserDto:
        """
        Find one user in the database and return his.

        :param user_id: id of user to find.
        :return: UserDto instance
        """
        async with async_session_maker() as session:
            stmt = (select(self.model).
                    where(self.model.id == user_id))
            user = await session.scalar(stmt)
            if not user:
                raise UserNotFoundError()
            return user.to_dto()

    async def find_all(self) -> list[UserDto]:
        """
        Find all users in the database and return them.

        :return: list of UserDto instances
        """
        async with async_session_maker() as session:
            stmt = select(self.model)
            users = await session.scalars(stmt)
            if not users:
                raise UserNotFoundError()
            users = [user.to_dto() for user in users]
            return users

    async def update_one(self, *args, **kwargs):
        """
        Now it is moc-method.
        :param args:
        :param kwargs:
        :return:
        """
        async with async_session_maker() as session:
            print('update_one')
            return True

    async def delete_one(self, *args, **kwargs):
        """
        Now it is moc-method.
        :param args:
        :param kwargs:
        :return:
        """
        async with async_session_maker() as session:
            print('delete_one')
            return True
