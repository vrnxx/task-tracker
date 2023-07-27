from src.repositories.task_repository import TaskRepository
from src.repositories.task_status_repository import TaskStatusRepository
from src.services.task_services import TaskService
from src.services.task_status_services import TaskStatusService


def task_service():
    return TaskService(TaskRepository)


def task_status_service():
    return TaskStatusService(TaskStatusRepository)
