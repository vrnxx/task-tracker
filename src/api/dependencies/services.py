from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.db import async_session_maker
from src.db.dao.status_dao import StatusDAO
from src.db.dao.task_dao import TaskDAO
from src.db.dao.user_dao import UserDAO
from src.services.status_service import TaskStatusService
from src.services.task_service import TaskService
from src.services.user_service import UserService
from src.api.dependencies.db import DBProvider, dao_provider
from src.db.holder import HolderDAO


def task_service(dao: HolderDAO = Depends(dao_provider)):
    return TaskService(dao)


def status_service():
    return TaskStatusService(StatusDAO)


def user_service():
    return UserService(UserDAO)
