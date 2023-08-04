from typing import TypeVar, Type, Generic, Sequence

from sqlalchemy import delete, func, ScalarResult
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.interfaces import ORMOption

from src.models.base import Base


Model = TypeVar('Model', bound=Base, covariant=True, contravariant=False)


class BaseDAO(Generic[Model]):
    def __init__(self, model: Type[Model], session: AsyncSession):
        self.model = model
        self.session = session

    async def _get_all(self, options: Sequence[ORMOption] = tuple()) -> Sequence[Model]:
        stmt = select(self.model).options(*options)
        result: ScalarResult[Model] = await self.session.scalars(stmt)
        return result.all()



