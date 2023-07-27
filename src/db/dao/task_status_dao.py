from sqlalchemy import select, insert
from src.db.db import async_session_maker
from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.models.task_status import TaskStatus
from src.schemas.task_status_schema import TaskStatusSchema


class TaskStatusDAO(AbstractDAO):
    model = TaskStatus

    async def add_one(self, status_data: dict) -> TaskStatusSchema:
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**status_data).
                    returning(self.model))
            new_status = await session.execute(stmt)
            await session.commit()
            return new_status.scalar_one()

    async def find_all(self) -> list[TaskStatusSchema]:
        async with async_session_maker() as session:
            stmt = select(self.model)
            statuses = await session.scalars(stmt)
            return statuses.all()

    async def find_one(self, *args, **kwargs):
        return {'find': 'one'}

    async def update_one(self, *args, **kwargs):
        return {'status update': [args, kwargs]}

    async def delete_one(self, *args, **kwargs):
        return {'status deleted': [args, kwargs]}
