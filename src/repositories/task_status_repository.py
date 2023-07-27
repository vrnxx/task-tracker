from src.models.task_status import TaskStatus
from src.utils.interfaces.sqlalchemy_repository import SQLAlchemyRepository


class TaskStatusRepository(SQLAlchemyRepository):
    model = TaskStatus
