from sqlalchemy.ext.asyncio import AsyncSession

from src.db.dao.status_dao import StatusDAO
from src.db.dao.task_dao import TaskDAO
from src.db.dao.user_dao import UserDAO


class HolderDAO:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.task = TaskDAO(session)
        self.status = StatusDAO(session)
        self.user = UserDAO(session)

    async def commit(self):
        await self.session.commit()
