from src.api.app_routers.task_router import router as task_router
from src.api.app_routers.task_status_router import router as status_router

routers = [status_router, task_router]
