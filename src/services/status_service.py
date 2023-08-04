from sqlalchemy.exc import SQLAlchemyError

from src.db.dao.status_dao import StatusDAO
from src.db.holder import HolderDAO
from src.models.dto.status import StatusDto
from src.schemas.status_schema import StatusAddSchema


class StatusService:
    def __init__(self, dao: HolderDAO):
        self.status_dao: StatusDAO = dao.status

    async def add_status(self, status: StatusAddSchema) -> StatusDto:
        status_dict = status.model_dump()
        try:
            new_status = await self.status_dao.add_one(status_dict)
            await self.status_dao.session.commit()
        except SQLAlchemyError as exc:
            await self.status_dao.session.rollback()
            raise exc
        return new_status

    async def get_all_statuses(self) -> list[StatusDto]:
        statuses = await self.status_dao.find_all()
        return statuses

    async def get_status(self, status_id: int) -> StatusDto:
        status = await self.status_dao.find_by_id(status_id)
        return status

    async def delete_status(self, status_id: int) -> StatusDto:
        try:
            deleted_status = await self.status_dao.delete_one(status_id)
            await self.status_dao.session.commit()
        except SQLAlchemyError as exc:
            await self.status_dao.session.rollback()
            raise exc
        return deleted_status

    async def update_status(
        self, status_id: int, status: StatusAddSchema
    ) -> StatusDto:
        status_dict = status.model_dump()
        try:
            updated_status = await self.status_dao.update_one(
                status_id, status_dict
            )
            await self.status_dao.session.commit()
        except SQLAlchemyError as exc:
            await self.status_dao.session.rollback()
            raise exc
        return updated_status
