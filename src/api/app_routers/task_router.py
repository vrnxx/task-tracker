from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies.services import task_service
from src.schemas.task_schema import TaskAddSchema
from src.services.task_service import TaskService
from src.models.dto.task import TaskDto

router = APIRouter(
    prefix='/task',
    tags=['task']
)


@router.get('/')
async def get_user_tasks(
        task_serv: Annotated[TaskService, Depends(task_service)]
) -> list[TaskDto]:
    tasks = await task_serv.get_tasks()
    return tasks


@router.get('/{task_id}')
async def get_task_by_id(
        task_id: int,
        task_serv: Annotated[TaskService, Depends(task_service)]
) -> TaskDto:
    task = await task_serv.get_task_by_id(task_id)
    return task


@router.post('/')
async def add_new_task(
        task_data: TaskAddSchema,
        task_serv: Annotated[TaskService, Depends(task_service)]
) -> TaskDto:
    added_task = await task_serv.add_new_task(task_data)
    return added_task


@router.put('/{task_id}')
async def update_task_data(
        task_id: int,
        new_task_data: TaskAddSchema,
        task_serv: Annotated[TaskService, Depends(task_service)]
) -> TaskDto:
    updated_task = await task_serv.update_task(task_id, new_task_data)
    return updated_task


@router.delete('/{task_id}')
async def delete_task_by_id(
        task_id: int,
        task_serv: Annotated[TaskService, Depends(task_service)]
) -> TaskDto:
    deleted_task = await task_serv.delete_task_by_id(task_id)
    return deleted_task

