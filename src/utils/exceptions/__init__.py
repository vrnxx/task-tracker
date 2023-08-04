from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.utils.exceptions.exceptions import (
    AlchemyError,
    StatusNotFoundError,
    TaskNotFoundError,
    UserEmailNotUnique,
    UserNotFoundError,
)


def setup(app: FastAPI):
    @app.exception_handler(AlchemyError)
    async def status_not_found_handler(request: Request, exc: AlchemyError):
        return JSONResponse(status_code=400, content={"detail": exc.message})

    @app.exception_handler(StatusNotFoundError)
    async def status_not_found_handler(
        request: Request, exc: StatusNotFoundError
    ):
        return JSONResponse(status_code=404, content={"detail": exc.message})

    @app.exception_handler(TaskNotFoundError)
    async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
        return JSONResponse(status_code=404, content={"detail": exc.message})

    @app.exception_handler(UserNotFoundError)
    async def task_not_found_handler(request: Request, exc: UserNotFoundError):
        return JSONResponse(status_code=404, content={"detail": exc.message})

    @app.exception_handler(UserEmailNotUnique)
    async def task_not_found_handler(request: Request, exc: UserEmailNotUnique):
        return JSONResponse(status_code=400, content={"detail": exc.message})
