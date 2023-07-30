from src.api.app_routers.task_router import router as task_router
from src.api.app_routers.status_router import router as status_router
from src.api.app_routers.user_router import router as user_router

routers = [status_router, task_router, user_router]
