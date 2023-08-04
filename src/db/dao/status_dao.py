from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.dao.base_dao import BaseDAO
from src.models.dto.status import StatusDto
from src.models.status import Status
from src.utils.exceptions.exc_mappers import status_exception_mapper


class StatusDAO(BaseDAO):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Status, session=session)

    async def find_all(self) -> list[StatusDto]:
        statuses = await self._get_all()
        return [status.to_dto() for status in statuses]

    @status_exception_mapper
    async def find_by_id(self, status_id: int) -> StatusDto:
        stmt = select(self.model).where(self.model.id == status_id)
        status = await self.session.scalar(stmt)
        return status.to_dto()

    async def add_one(self, status_data: dict) -> StatusDto:
        stmt = insert(self.model).values(**status_data).returning(self.model)
        added_status = await self.session.scalar(stmt)
        return added_status.to_dto()

    @status_exception_mapper
    async def update_one(
        self, status_id: int, new_status_data: dict
    ) -> StatusDto:
        stmt = (
            update(self.model)
            .where(self.model.id == status_id)
            .values(**new_status_data)
            .returning(self.model)
        )
        updated_status = await self.session.scalar(stmt)
        return updated_status.to_dto()

    @status_exception_mapper
    async def delete_one(self, status_id: int) -> StatusDto:
        stmt = (
            delete(self.model)
            .where(self.model.id == status_id)
            .returning(self.model)
        )
        deleted_task = await self.session.scalar(stmt)
        return deleted_task.to_dto()
