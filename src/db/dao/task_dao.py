from sqlalchemy import delete, insert, select, update

from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.db.db import async_session_maker
from src.models.dto.task import TaskDto
from src.models.task import Task
from src.utils.exceptions import TaskNotFoundError


class TaskDAO(AbstractDAO):
    """
    Class for management of Task-model in the database.

    Implements AbstractDAO methods.
    Returned values from methods are TaskDto instances.
    """
    model = Task

    async def add_one(self, task_data: dict) -> TaskDto:
        """
        Add a new task to database.

        :param task_data: dictionary
        :return: new task: TaskDto instance
        """
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**task_data).
                    returning(self.model))
            new_task = await session.scalar(stmt)
            await session.commit()
            return new_task.to_dto()
        
    async def find_all(self) -> list[TaskDto]:
        """
        Find all tasks in database.

        :return: list of tasks: TaskDto
        """
        async with async_session_maker() as session:
            stmt = select(self.model)
            tasks = await session.scalars(stmt)
            return [task.to_dto() for task in tasks]
        
    async def find_one(self, task_id: int) -> TaskDto:
        """
        Find one task in database.

        :raise: TaskNotFoundError: if task not found
        :param task_id: number of task
        :return: task: TaskDto instance
        """
        async with async_session_maker() as session:
            stmt = (select(self.model).
                    where(self.model.id == task_id))
            task = await session.scalar(stmt)
            print(task)
            if not task:
                raise TaskNotFoundError()

            return task.to_dto()

    async def update_one(self, task_id: int,
                         new_data: dict) -> TaskDto:
        """
        Update one task in database.

        :raise: TaskNotFoundError: if task not found
        :param task_id: id of task
        :param new_data: dictionary with new data
        :return: updated task: TaskDto instance
        """
        async with async_session_maker() as session:
            stmt = (update(self.model).
                    where(self.model.id == task_id).
                    values(**new_data).
                    returning(self.model))
            updated_task = await session.scalar(stmt)
            await session.commit()
            if not updated_task:
                raise TaskNotFoundError()
            return updated_task.to_dto()
            
    async def delete_one(self, task_id: int) -> TaskDto:
        """
        Delete one task in database and return deleted task.

        :raise: TaskNotFoundError: if task not found
        :param task_id: id of task
        :return: deleted task: TaskDto instance
        """
        async with async_session_maker() as session:
            stmt = (delete(self.model).
                    where(self.model.id == task_id).
                    returning(self.model))

            deleted_task = await session.scalar(stmt)
            await session.commit()
            if not deleted_task:
                raise TaskNotFoundError()

            return deleted_task.to_dto()
