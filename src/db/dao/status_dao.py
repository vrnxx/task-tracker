from sqlalchemy import select, insert, delete, update
from src.db.db import async_session_maker
from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.models.status import Status
from src.schemas.status_schema import StatusSchema
from src.exceptions.status_exceptions import StatusNotFoundError


class StatusDAO(AbstractDAO):
    model = Status

    async def add_one(self, status_data: dict) -> StatusSchema:
        """
        Add a new status to the database

        :param status_data: status data to add
        :return: new_status: StatusSchema
        """
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**status_data).
                    returning(self.model))
            new_status = await session.execute(stmt)
            await session.commit()

            return new_status.scalar_one()

    async def find_one(self, status_id: int) -> StatusSchema:
        """
        Find a status in the database.

        :raise: StatusNotFoundError if the status is not found.
        :param status_id: id of the status to find.
        :return: status: StatusSchema
        """
        async with async_session_maker() as session:
            stmt = (select(self.model).
                    where(self.model.id == status_id))
            status = await session.scalar(stmt)

            if not status:
                raise StatusNotFoundError(status_id=status_id)

            return status

    async def find_all(self) -> list[StatusSchema]:
        """
        Find all statuses in the database.

        :return: statuses: list[StatusSchema]
        """
        async with async_session_maker() as session:
            stmt = select(self.model)
            statuses = await session.scalars(stmt)
            return statuses.all()

    async def update_one(self, status_id: int,
                         status_data: dict) -> StatusSchema:
        """
        Update a status in the database.

        :raise: StatusNotFoundError if the status is not found.
        :param status_id: id of the status to update.
        :param status_data: status data to update.
        :return: updated_status: StatusSchema
        """
        async with async_session_maker() as session:
            stmt = (update(self.model).
                    where(self.model.id == status_id).
                    values(**status_data).
                    returning(self.model))
            updated_status = await session.scalar(stmt)
            await session.commit()

            if not updated_status:
                raise StatusNotFoundError(status_id=status_id)

            return updated_status

    async def delete_one(self, status_id: int) -> StatusSchema:
        """
        Delete a status from the database and return deleted status.

        :raise: StatusNotFoundError if the status is not found.
        :param status_id: id of the status to delete.
        :return: deleted_status: StatusSchema
        """
        async with async_session_maker() as session:
            stmt = (delete(self.model).
                    where(self.model.id == status_id).
                    returning(self.model))
            deleted_status = await session.scalar(stmt)
            await session.commit()

            if not deleted_status:
                raise StatusNotFoundError(status_id=status_id)

            return deleted_status
