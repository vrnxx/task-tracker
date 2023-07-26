from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.db import get_async_session
from src.schemas.task_status_schema import TaskStatusAddSchema
from src.models.task_status import TaskStatus


router = APIRouter(
    prefix='/status',
    tags=['task status']
)


@router.get('/')
async def get_all_statuses(session: Annotated[AsyncSession, Depends(get_async_session)]):
    query = select(TaskStatus)
    res = await session.scalars(query)
    statuses = res.all()
    return {'statuses': statuses}


@router.post('/')
async def create_new_status(new_status: TaskStatusAddSchema,
                            session: Annotated[AsyncSession, Depends(get_async_session)]):
    stmt = insert(TaskStatus).values(new_status.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {'status add': new_status}
