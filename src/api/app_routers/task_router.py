from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from src.schemas.task_schema import TaskAddSchema, TaskSchema
from src.db.db import get_async_session
from src.models.task import Task

router = APIRouter(
    prefix='/task',
    tags=['task']
)


@router.get('/', response_model=list[TaskSchema])
async def get_tasks(session: Annotated[AsyncSession, Depends(get_async_session)]):
    query = select(Task)
    res = await session.scalars(query)
    tasks = res.all()
    return tasks


@router.post('/')
async def create_new_task(new_task: TaskAddSchema,
                          session: Annotated[AsyncSession, Depends(get_async_session)]):
    stmt = insert(Task).values(new_task.model_dump()).returning(Task)
    res = await session.execute(stmt)
    await session.commit()
    created_task = [t[0].to_read_model() for t in res]
    return {'status': 'successful', 'data': created_task}
