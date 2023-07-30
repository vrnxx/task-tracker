from sqlalchemy import select, insert, update, delete
from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.models.task import Task
from src.db.db import async_session_maker
from src.schemas.task_schema import TaskSchema
from src.utils.exceptions import TaskNotFoundError


class TaskDAO(AbstractDAO):
    model = Task

    async def add_one(self, task_data: dict) -> TaskSchema:
        """
        Add a new task to database.

        :param task_data: dictionary
        :return: new task: TaskSchema
        """
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**task_data).
                    returning(self.model))
            res = await session.scalar(stmt)
            await session.commit()
            return res
        
    async def find_all(self) -> list[TaskSchema]:
        """
        Find all tasks in database.

        :return: list of tasks: TaskSchema
        """
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.scalars(stmt)
            return res.all()
        
    async def find_one(self, task_id: int):
        """
        Find one task in database.

        :raise: TaskNotFoundError: if task not found
        :param task_id: number of task
        :return: task: TaskSchema
        """
        async with async_session_maker() as session:
            stmt = (select(self.model).
                    where(self.model.id == task_id))
            res = await session.scalar(stmt)
            if not res:
                raise TaskNotFoundError()

            return res.scalar_one()

    async def update_one(self, task_id: int,
                         new_data: dict) -> TaskSchema:
        """
        Update one task in database.

        :raise: TaskNotFoundError: if task not found
        :param task_id: id of task
        :param new_data: dictionary with new data
        :return: updated task: TaskSchema
        """
        async with async_session_maker() as session:
            stmt = (update(self.model).
                    where(self.model.id == task_id).
                    values(**new_data).
                    returning(self.model))
            res = await session.scalar(stmt)
            await session.commit()
            if not res:
                raise TaskNotFoundError()
            return res
            
    async def delete_one(self, task_id: int) -> TaskSchema:
        """
        Delete one task in database and return deleted task.

        :raise: TaskNotFoundError: if task not found
        :param task_id: id of task
        :return: deleted task: TaskSchema
        """
        async with async_session_maker() as session:
            stmt = (delete(self.model).
                    where(self.model.id == task_id).
                    returning(self.model))

            deleted_task = await session.scalar(stmt)
            await session.commit()
            if not deleted_task:
                raise TaskNotFoundError()

            return deleted_task
