from src.schemas.task_schema import TaskAddSchema
from src.utils.interfaces.abstract_repository import AbstractRepository


class TaskService:
    def __init__(self, task_repo: AbstractRepository):
        self.task_repo: AbstractRepository = task_repo()

    async def get_tasks(self):
        tasks = await self.task_repo.find_all()
        return tasks

    async def get_task(self, task_id: int):
        task = await self.task_repo.find_one(task_id)
        return task

    async def add_task(self, task: TaskAddSchema):
        task_dict = task.model_dump()
        new_task = await self.task_repo.add_one(task_dict)
        return new_task

    async def delete_task(self, task_id: int):
        deleted_id = await self.task_repo.delete_one(task_id)
        return deleted_id
