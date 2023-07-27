from fastapi.exceptions import HTTPException
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import NoResultFound

from src.db.db import async_session_maker
from src.db.dao.interfaces.abstract_dao import AbstractDAO


class SQLAlchemyRepository(AbstractDAO):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def update_one(self, obj_id: int, new_data: dict):
        async with async_session_maker() as session:
            stmt = (update(self.model).
                    where(self.model.id == obj_id).
                    values(**new_data).returning(self.model))
            try:
                res = await session.execute(stmt)
                await session.commit()
                return res.scalar_one()
            except NoResultFound:
                raise HTTPException(
                    status_code=404,
                    detail=f'Object with id {obj_id} not found'
                )

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.scalars(stmt)
            return res.all()

    async def find_one(self, obj_id: int):
        async with async_session_maker() as session:
            stmt = select(self.model).where(self.model.id == obj_id)
            try:
                res = await session.execute(stmt)
                return res.scalar_one()
            except NoResultFound:
                raise HTTPException(
                    status_code=404,
                    detail=f'Object with id {obj_id} not found'
                )

    async def delete_one(self, obj_id: int) -> int:
        async with async_session_maker() as session:
            stmt = (delete(self.model).
                    where(self.model.id == obj_id).
                    returning(self.model.id))
            res = await session.execute(stmt)
            await session.commit()
            try:
                return obj_id
            except NoResultFound:
                raise HTTPException(
                    status_code=404,
                    detail=f'Unable to delete object with id {obj_id}. '
                           f'Not found'
                )
