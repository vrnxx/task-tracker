from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies.services import status_service
from src.models.dto.status import StatusDto
from src.schemas.status_schema import StatusAddSchema
from src.services.status_service import StatusService

router = APIRouter(prefix="/status", tags=["status"])


@router.get("/{status_id}")
async def get_status_by_id(
    status_id: int,
    status_service: Annotated[StatusService, Depends(status_service)],
) -> StatusDto:
    status = await status_service.get_status(status_id)
    return status


@router.get("/")
async def get_all_statuses(
    status_service: Annotated[StatusService, Depends(status_service)]
) -> list[StatusDto]:
    tasks = await status_service.get_all_statuses()
    return tasks


@router.post("/", status_code=201)
async def add_new_status(
    new_status: StatusAddSchema,
    status_service: Annotated[StatusService, Depends(status_service)],
) -> StatusDto:
    created_status = await status_service.add_status(new_status)
    return created_status


@router.delete("/{status_id}")
async def delete_status(
    status_id: int,
    status_service: Annotated[StatusService, Depends(status_service)],
) -> StatusDto:
    deleted_status = await status_service.delete_status(status_id)
    return deleted_status


@router.put("/{status_id}")
async def update_status(
    status_id: int,
    new_status: StatusAddSchema,
    status_service: Annotated[StatusService, Depends(status_service)],
) -> StatusDto:
    updated_status = await status_service.update_status(status_id, new_status)
    return updated_status
