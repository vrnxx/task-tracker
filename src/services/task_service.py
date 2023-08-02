from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.schemas.task_schema import TaskAddSchema


class TaskService:
    def __init__(self, task_dao: AbstractDAO):
        self.task_dao: AbstractDAO = task_dao()

    async def get_user_tasks(self, user_id: int):
        tasks = await self.task_dao.find_all(user_id)
        return tasks

    async def get_task(self, task_id: int):
        task = await self.task_dao.find_one(task_id)
        return task

    async def add_task(self, task: TaskAddSchema):
        task_dict = task.model_dump()
        new_task = await self.task_dao.add_one(task_dict)
        return new_task

    async def update_task(self, task_id: int, new_data: TaskAddSchema):
        task_dict = new_data.model_dump()
        updated_task = await self.task_dao.update_one(task_id, task_dict)
        return updated_task

    async def delete_task(self, task_id: int):
        deleted_id = await self.task_dao.delete_one(task_id)
        return deleted_id
