from src.utils.interfaces.abstract_repository import AbstractRepository
from src.schemas.task_schema import TaskAddSchema


class TaskService:
    def __init__(self, task_repo: AbstractRepository):
        self.task_repo: AbstractRepository = task_repo()

    async def get_tasks(self):
        tasks = await self.task_repo.find_all()
        return tasks

    async def add_task(self, task: TaskAddSchema):
        task_dict = task.model_dump()
        new_task = await self.task_repo.add_one(task_dict)
        return new_task
