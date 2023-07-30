from src.db.dao.status_dao import StatusDAO
from src.db.dao.task_dao import TaskDAO
from src.db.dao.user_dao import UserDAO
from src.services.status_service import TaskStatusService
from src.services.task_service import TaskService
from src.services.user_service import UserService


def task_service():
    return TaskService(TaskDAO)


def status_service():
    return TaskStatusService(StatusDAO)


def user_service():
    return UserService(UserDAO)
