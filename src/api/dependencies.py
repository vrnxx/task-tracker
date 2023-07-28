from src.db.dao.task_dao import TaskDAO
from src.db.dao.status_dao import StatusDAO
from src.services.task_services import TaskService
from src.services.status_services import TaskStatusService


def task_service():
    return TaskService(TaskDAO)


def status_service():
    return TaskStatusService(StatusDAO)
