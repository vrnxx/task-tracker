from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import task_service
from src.schemas.task_schema import TaskAddSchema, TaskSchema
from src.services.task_service import TaskService
from src.models.dto.task import TaskDto

router = APIRouter(
    prefix='/task',
    tags=['task']
)


@router.get('/{task_id}', response_model=TaskSchema)
async def get_task(task_id: int,
                   task_serv: Annotated[TaskService, Depends(task_service)]):
    task = await task_serv.get_task(task_id)
    return task


@router.get('/user_tasks/{user_id}')
async def get_user_tasks(
        user_id: int,
        task_serv: Annotated[TaskService, Depends(task_service)]
) -> list[TaskDto]:
    tasks = await task_serv.get_user_tasks(user_id)
    return tasks


@router.post("/")
async def add_task(
        task: TaskAddSchema,
        task_serv: Annotated[TaskService, Depends(task_service)]):
    new_task = await task_serv.add_task(task)
    return new_task


@router.put('/{task_id}')
async def update_task(
        task_id: int,
        new_data: TaskAddSchema,
        task_serv: Annotated[TaskService, Depends(task_service)]):
    updated_task = await task_serv.update_task(task_id, new_data)
    return updated_task


@router.delete('/')
async def delete_task(task_id: int,
                      task_serv: Annotated[TaskService,
                      Depends(task_service)]):
    deleted_id = await task_serv.delete_task(task_id)
    return deleted_id
