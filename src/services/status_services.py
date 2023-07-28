from src.schemas.status_schema import StatusAddSchema
from src.db.dao.interfaces.abstract_dao import AbstractDAO


class TaskStatusService:
    def __init__(self, status_dao: AbstractDAO):
        self.status_dao: AbstractDAO = status_dao()

    async def get_all_statuses(self):
        tasks = await self.status_dao.find_all()
        return tasks

    async def add_status(self, status: StatusAddSchema):
        status_dict = status.model_dump()
        new_status = await self.status_dao.add_one(status_dict)
        return new_status

    async def get_status(self, status_id: int):
        status = await self.status_dao.find_one(status_id)
        return status

    async def delete_status(self, status_id: int):
        deleted_status = await self.status_dao.delete_one(status_id)
        return deleted_status

    async def update_status(self, status_id: int, status: StatusAddSchema):
        status_dict = status.model_dump()
        updated_status = await self.status_dao.update_one(status_id, status_dict)
        return updated_status





