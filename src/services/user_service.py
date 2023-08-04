from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from src.db.dao.user_dao import UserDAO
from src.db.holder import HolderDAO
from src.models.dto.user import UserDto
from src.schemas.user_schema import UserAddSchema
from src.utils.exceptions.exceptions import UserEmailNotUnique


class UserService:
    def __init__(self, dao: HolderDAO):
        self.user_dao: UserDAO = dao.user

    async def get_user_by_id(self, user_id: int) -> UserDto:
        try:
            user = await self.user_dao.find_one_by_id(user_id)
        except SQLAlchemyError as exc:
            await self.user_dao.session.rollback()
            raise exc
        return user

    async def get_all_users(self) -> list[UserDto]:
        users = await self.user_dao.find_all()
        return users

    async def add_user(self, user: UserAddSchema) -> UserDto:
        try:
            new_user = await self.user_dao.add_one(user.model_dump())
            await self.user_dao.session.commit()
        except IntegrityError:
            await self.user_dao.session.rollback()
            raise UserEmailNotUnique
        except SQLAlchemyError as exc:
            await self.user_dao.session.rollback()
            raise exc

        return new_user

    async def update_user(self, user_id: int,
                          new_data: UserAddSchema) -> UserDto:
        try:
            updated_user = await self.user_dao.update_one(
                user_id, new_data.model_dump())

            await self.user_dao.session.commit()
        except IntegrityError:
            await self.user_dao.session.rollback()
            raise UserEmailNotUnique
        except SQLAlchemyError as exc:
            await self.user_dao.session.rollback()
            raise exc
        return updated_user

    async def delete_user(self, user_id: int) -> UserDto:
        try:
            deleted_user = await self.user_dao.delete_one_by_id(user_id)
            await self.user_dao.session.commit()
        except SQLAlchemyError as exc:
            await self.user_dao.session.rollback()
            raise exc

        return deleted_user
