import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from src.api import app_routers, dependencies
from src.config import (
    DB_HOST_TEST,
    DB_NAME_TEST,
    DB_PASS_TEST,
    DB_PORT_TEST,
    DB_USER_TEST,
)
from src.db.db import async_session_maker
from src.utils import exceptions

DATABASE_URL = f"postgresql+asyncpg://{DB_USER_TEST}:{DB_PASS_TEST}@{DB_HOST_TEST}:{DB_PORT_TEST}/{DB_NAME_TEST}"

engine_test = create_async_engine(DATABASE_URL)


async_session_maker = sessionmaker(
    bind=engine_test,
    class_=AsyncSession,
    autoflush=False,
    expire_on_commit=False,
)


def main_test():
    test_app = FastAPI(title="test_ttracker")
    exceptions.setup(app=test_app)
    app_routers.setup(app=test_app)
    dependencies.setup(app=test_app, pool=async_session_maker)

    return test_app


def run_test_server():
    uvicorn.run(app="src:main_test", host="127.0.0.1", port=9000, reload=True)


if __name__ == "__main__":
    run_test_server()
