from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.db.holder import HolderDAO


def dao_provider() -> HolderDAO:
    raise NotImplementedError


class DbProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def dao(self):
        async with self.pool() as session:
            yield HolderDAO(session=session)
