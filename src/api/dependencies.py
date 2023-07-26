from src.services.task_services import TaskService
from src.repositories.task_repository import TaskRepository


def task_service():
    return TaskService(TaskRepository)
