import uvicorn
from fastapi import FastAPI

from src.api import app_routers, dependencies
from src.db.db import async_session_maker
from src.utils import exceptions


def main() -> FastAPI:
    app = FastAPI(title="t_tracker", version="0.1.1")

    exceptions.setup(app=app)
    app_routers.setup(app=app)
    dependencies.setup(app=app, pool=async_session_maker)

    return app


def run():
    uvicorn.run("src:main", host="127.0.0.1", port=8000, reload=True)


if __name__ == "__main__":
    run()
