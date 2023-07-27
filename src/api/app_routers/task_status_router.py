from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import task_status_service
from src.schemas.task_status_schema import TaskStatusAddSchema
from src.services.task_status_services import TaskStatusService

router = APIRouter(
    prefix='/status',
    tags=['task status']
)


@router.get('/')
async def get_all_statuses(task_status_serv:
Annotated[TaskStatusService, Depends(task_status_service)]):
    tasks = await task_status_serv.get_all_statuses()
    return tasks


@router.post('/')
async def add_new_status(new_status: TaskStatusAddSchema,
                         task_status_serv: Annotated[TaskStatusService,
                         Depends(task_status_service)]):
    created_status = await task_status_serv.add_status(new_status)
    return created_status
