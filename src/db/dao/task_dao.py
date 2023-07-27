from fastapi.exceptions import HTTPException
from sqlalchemy import select, insert, update, delete
from sqlalchemy.exc import NoResultFound
from src.db.dao.interfaces.abstract_dao import AbstractDAO
from src.models.task import Task
from src.db.db import async_session_maker


class TaskDAO(AbstractDAO):
    model = Task

    async def add_one(self, task_data: dict):
        async with async_session_maker() as session:
            stmt = (insert(self.model).
                    values(**task_data).
                    returning(self.model))
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()
        
    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.scalars(stmt)
            return res.all()
        
    async def find_one(self, task_id: int):
        async with async_session_maker() as session:
            stmt = (select(self.model).
                    where(self.model.id == task_id))
            try:
                res = await session.execute(stmt)
                return res.scalar_one()
            except NoResultFound:
                raise HTTPException(
                    status_code=404,
                    detail=f'Task with id {task_id} not found'
                )
    
    async def update_one(self, task_id: int, new_data: dict):
        async with async_session_maker() as session:
            stmt = (update(self.model).
                    where(self.model.id == task_id).
                    values(**new_data).
                    returning(self.model))
            try:
                res = await session.execute(stmt)
                await session.commit()
                return res.scalar_one()
            except NoResultFound:
                raise HTTPException(
                    status_code=404,
                    detail=f'Task with id {task_id} not found'
                )
            
    async def delete_one(self, task_id: int):
        async with async_session_maker() as session:
            stmt = (delete(self.model).
                    where(self.model.id == task_id).
                    returning(self.model.id))
            try:
                deleted_id = await session.execute(stmt)
                await session.commit()
                return deleted_id.scalar_one()
            except NoResultFound:
                raise HTTPException(
                    status_code=404,
                    detail=f'Unable to delete task with id {task_id}. '
                           f'Not found'
                )








