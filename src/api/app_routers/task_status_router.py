from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db import get_async_session
from src.schemas.task_status_schema import TaskStatusAddSchema, TaskStatusSchema
from src.models.task_status import TaskStatus

router = APIRouter(
    prefix='/status',
    tags=['task status']
)


@router.get('/')
async def get_all_statuses(session: Annotated[AsyncSession,
Depends(get_async_session)]) -> list[TaskStatusSchema]:
    query = select(TaskStatus)
    res = await session.scalars(query)
    statuses = res.all()
    return list(statuses)


@router.post('/')
async def create_new_status(new_status: TaskStatusAddSchema,
session: Annotated[AsyncSession, Depends(get_async_session)]) -> dict:
    stmt = insert(TaskStatus).values(new_status.model_dump()).returning(TaskStatus)
    res = await session.execute(stmt)
    await session.commit()
    created_status = [r[0].to_read_model() for r in res]
    return {'status add': created_status}
