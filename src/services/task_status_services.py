from src.schemas.task_status_schema import TaskStatusAddSchema
from src.utils.interfaces.abstract_repository import AbstractRepository


class TaskStatusService:
    def __init__(self, task_status_repo: AbstractRepository):
        self.task_status_repo = task_status_repo()

    async def get_all_statuses(self):
        tasks = await self.task_status_repo.find_all()
        return tasks

    async def add_status(self, status: TaskStatusAddSchema):
        status_dict = status.model_dump()
        new_status = await self.task_status_repo.add_one(status_dict)
        return new_status
