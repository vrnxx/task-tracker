from sqlalchemy import select, insert
from src.utils.interfaces.abstract_repository import AbstractRepository
from src.db.db import async_session_maker


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def find_all(self):
        async with async_session_maker() as session:
            stmt = select(self.model)
            res = await session.scalars(stmt)
            return res.all()

