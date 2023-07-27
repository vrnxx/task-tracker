from src.db.dao.task_dao import TaskDAO
from src.db.dao.task_status_dao import TaskStatusDAO
from src.services.task_services import TaskService
from src.services.task_status_services import TaskStatusService


def task_service():
    return TaskService(TaskDAO)


def task_status_service():
    return TaskStatusService(TaskStatusDAO)
