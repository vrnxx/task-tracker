from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.dao.base_dao import BaseDAO
from src.models.dto.task import TaskDto
from src.models.task import Task
from src.utils.exceptions.exc_mappers import task_exception_mapper


class TaskDAO(BaseDAO[Task]):
    def __init__(self, session: AsyncSession):
        super().__init__(model=Task, session=session)

    async def find_all(self) -> list[TaskDto]:
        tasks = await self._get_all()
        return [task.to_dto() for task in tasks]

    @task_exception_mapper
    async def find_one_by_id(self, task_id: int) -> TaskDto:
        stmt = select(self.model).where(self.model.id == task_id)
        task = await self.session.scalar(stmt)

        return task.to_dto()

    async def add_one(self, task_data: dict) -> TaskDto:
        stmt = insert(self.model).values(**task_data).returning(self.model)
        added_task = await self.session.scalar(stmt)

        return added_task.to_dto()

    @task_exception_mapper
    async def update_one(self, task_id: int, new_task_data: dict) -> TaskDto:
        stmt = (
            update(self.model)
            .where(self.model.id == task_id)
            .values(**new_task_data)
            .returning(self.model)
        )
        updated_task_data = await self.session.scalar(stmt)

        return updated_task_data.to_dto()

    @task_exception_mapper
    async def delete_one(self, task_id: int) -> TaskDto:
        stmt = (delete(self.model).
                where(self.model.id == task_id).
                returning(self.model))
        deleted_task = await self.session.scalar(stmt)

        return deleted_task.to_dto()
