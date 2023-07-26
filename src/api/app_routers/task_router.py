from typing import Annotated

from fastapi import APIRouter, Depends
from src.services.task_services import TaskService
from src.api.dependencies import task_service
from src.schemas.task_schema import TaskAddSchema

router = APIRouter(
    prefix='/task',
    tags=['task']
)


@router.get('/')
async def get_tasks(task_serv: Annotated[TaskService, Depends(task_service)]):
    tasks = await task_serv.get_tasks()
    return tasks


@router.post("")
async def add_task(
        task: TaskAddSchema,
        tasks_service: Annotated[TaskService, Depends(task_service)]):
    new_task = await tasks_service.add_task(task)
    return new_task
