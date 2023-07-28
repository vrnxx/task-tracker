from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import status_service
from src.schemas.status_schema import StatusAddSchema
from src.services.status_services import TaskStatusService

router = APIRouter(
    prefix='/status',
    tags=['task status']
)


@router.get('/')
async def get_all_statuses(status_service:
Annotated[TaskStatusService, Depends(status_service)]):
    tasks = await status_service.get_all_statuses()
    return tasks


@router.get('/{status_id}')
async def get_status_by_id(status_id: int,
                           status_service: Annotated[TaskStatusService,
                           Depends(status_service)]):
    status = await status_service.get_status(status_id)
    return status


@router.post('/')
async def add_new_status(new_status: StatusAddSchema,
                         status_service: Annotated[TaskStatusService,
                         Depends(status_service)]):
    created_status = await status_service.add_status(new_status)
    return created_status


@router.delete('/{status_id}')
async def delete_status(status_id: int,
                        status_service: Annotated[TaskStatusService,
                        Depends(status_service)]):
    deleted_status = await status_service.delete_status(status_id)
    return deleted_status


@router.put('/{status_id}')
async def update_status(status_id: int,
                         new_status: StatusAddSchema,
                         status_service: Annotated[TaskStatusService, Depends(status_service)]):
    updated_status = await status_service.update_status(status_id, new_status)
    return updated_status
