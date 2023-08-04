from typing import Annotated

from fastapi import Depends

from src.api.dependencies.db import dao_provider
from src.db.holder import HolderDAO
from src.services.status_service import StatusService
from src.services.task_service import TaskService
from src.services.user_service import UserService


def task_service(dao: Annotated[HolderDAO, Depends(dao_provider)]
                 ) -> TaskService:
    return TaskService(dao)


def status_service(dao: Annotated[HolderDAO, Depends(dao_provider)]
                   ) -> StatusService:
    return StatusService(dao)


def user_service(dao: Annotated[HolderDAO, Depends(dao_provider)]
                 ) -> UserService:
    return UserService(dao)
