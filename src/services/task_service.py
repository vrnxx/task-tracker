from sqlalchemy.exc import SQLAlchemyError

from src.db.dao.task_dao import TaskDAO
from src.db.holder import HolderDAO
from src.models.dto.task import TaskDto
from src.schemas.task_schema import TaskAddSchema


class TaskService:
    """fldsfkds;lfkdsf;ldsfk;ldskf;ldskf;dsl;fkdsl;fkdsf;lkdsf131231l;kfds;lfkdsl;fkds;lkfds;lfkds;lkdsf;lk;l;ldskf;lsfdsklds;dsk;ldskds;ldskf;lds"""

    def __init__(self, dao: HolderDAO):
        self.task_dao: TaskDAO = dao.task

    async def add_new_task(self, task_data: TaskAddSchema) -> TaskDto:
        try:
            added_task = await self.task_dao.add_one(task_data.model_dump())
            await self.task_dao.session.commit()
        except SQLAlchemyError as exc:
            await self.task_dao.session.rollback()
            raise exc

        return added_task

    async def get_tasks(self) -> list[TaskDto]:
        tasks = await self.task_dao.find_all()

        return tasks

    async def get_task_by_id(self, task_id: int) -> TaskDto:
        task = await self.task_dao.find_one_by_id(task_id)
        return task

    async def update_task(
        self, task_id: int, task_data: TaskAddSchema
    ) -> TaskDto:
        try:
            updated_task = await self.task_dao.update_one(
                task_id, task_data.model_dump()
            )

            await self.task_dao.session.commit()
        except SQLAlchemyError as exc:
            await self.task_dao.session.rollback()
            raise exc

        return updated_task

    async def delete_task_by_id(self, task_id: int) -> TaskDto:
        try:
            deleted_task = await self.task_dao.delete_one(task_id)
            await self.task_dao.session.commit()
        except SQLAlchemyError as exc:
            await self.task_dao.session.rollback()
            raise exc

        return deleted_task
