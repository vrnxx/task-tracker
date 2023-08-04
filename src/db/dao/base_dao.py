from typing import Generic, Sequence, Type, TypeVar

from sqlalchemy import ScalarResult, delete, func, select
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
        return result



