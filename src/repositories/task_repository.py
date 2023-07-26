from src.models.task import Task
from src.utils.interfaces.sqlalchemy_repository import SQLAlchemyRepository


class TaskRepository(SQLAlchemyRepository):
    model = Task
