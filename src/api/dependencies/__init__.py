from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from src.api.dependencies.db import DbProvider, dao_provider


def setup(app: FastAPI, pool: async_sessionmaker[AsyncSession]):
    db_provider = DbProvider(pool=pool)

    app.dependency_overrides[dao_provider] = db_provider.dao

