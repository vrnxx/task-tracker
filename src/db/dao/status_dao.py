from sqlalchemy import delete, insert, select, update

from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.db.db import async_session_maker
from src.models.dto.status import StatusDto
from src.models.status import Status
from src.utils.exceptions import StatusNotFoundError


class StatusDAO(AbstractDAO):
    """
    Class for management of Status-model in the database.

    Implements AbstractDAO methods.
    Returned values from methods are StatusDto instances.
    """
    model = Status

    async def add_one(self, status_data: dict) -> StatusDto:
        """
        Add a new status to the database.

        :param status_data: status data to add
        :return: new_status: StatusDto instance
        """
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**status_data).
                    returning(self.model))
            new_status = await session.scalar(stmt)
            await session.commit()

            return new_status.to_dto()

    async def find_one(self, status_id: int) -> StatusDto:
        """
        Find a status in the database.

        :raise StatusNotFoundError if the status is not found.
        :param status_id: id of the status to find.
        :return: status: StatusDto instance
        """
        async with async_session_maker() as session:
            stmt = (select(self.model).
                    where(self.model.id == status_id))
            status = await session.scalar(stmt)

            if not status:
                raise StatusNotFoundError()

            return status.to_dto()

    async def find_all(self) -> list[StatusDto]:
        """
        Find all statuses in the database.

        :return: statuses - list[StatusDto]
        """
        async with async_session_maker() as session:
            stmt = select(self.model)
            statuses = await session.scalars(stmt)
            if not statuses:
                raise StatusNotFoundError
            statuses = [status.to_dto() for status in statuses]
            return statuses

    async def update_one(self, status_id: int,
                         status_data: dict) -> StatusDto:
        """
        Update a status in the database.

        :raise StatusNotFoundError if the status is not found.
        :param status_id: id of the status to update.
        :param status_data: status data to update.
        :return: updated_status: StatusDto instance
        """
        async with async_session_maker() as session:
            stmt = (update(self.model).
                    where(self.model.id == status_id).
                    values(**status_data).
                    returning(self.model))
            updated_status = await session.scalar(stmt)
            await session.commit()

            if not updated_status:
                raise StatusNotFoundError()

            return updated_status.to_dto()

    async def delete_one(self, status_id: int) -> StatusDto:
        """
        Delete a status from the database and return deleted status.

        :raise StatusNotFoundError if the status is not found.
        :param status_id: id of the status to delete.
        :return: deleted_status: StatusDto instance
        """
        async with async_session_maker() as session:
            stmt = (delete(self.model).
                    where(self.model.id == status_id).
                    returning(self.model))
            deleted_status = await session.scalar(stmt)
            await session.commit()

            if not deleted_status:
                raise StatusNotFoundError()

            return deleted_status.to_dto()
