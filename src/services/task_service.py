from src.db.holder import HolderDAO
from src.db.dao.task_dao import TaskDAO
from src.schemas.task_schema import TaskAddSchema
from src.models.dto.task import TaskDto


class TaskService:
    def __init__(self, dao: HolderDAO):
        self.task_dao: TaskDAO = dao.task

    async def add_new_task(self, task_data: TaskAddSchema) -> TaskDto:
        added_task = await self.task_dao.add_one(task_data.model_dump())
        await self.task_dao.session.commit()
        return added_task

    async def get_tasks(self) -> list[TaskDto]:
        tasks = await self.task_dao.find_all()
        return tasks

    async def get_task_by_id(self, task_id: int) -> TaskDto:
        task = await self.task_dao.find_by_id(task_id)
        return task

    async def update_task(self, task_id: int,
                          task_data: TaskAddSchema) -> TaskDto:
        updated_task = await self.task_dao.update_one(task_id,
                                                      task_data.model_dump())
        await self.task_dao.session.commit()
        return updated_task

    async def delete_task_by_id(self, task_id: int) -> TaskDto:
        deleted_task = await self.task_dao.delete_one(task_id)
        await self.task_dao.session.commit()
        return deleted_task

