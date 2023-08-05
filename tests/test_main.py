from httpx import AsyncClient
from sqlalchemy import insert, select

from src.models import dto
from src.models.status import Status
from tests.conftest import ac, async_session_maker


async def test_add_status():
    async with async_session_maker() as session:
        stmt = insert(Status).values(id=1, title="test_status")
        await session.execute(stmt)
        await session.commit()

        query = select(Status)
        res = await session.scalar(query)

        assert res.to_dto() == dto.StatusDto(
            id=1, title="test_status"
        ), "Статус не добавлен"


async def test_add_new_user(ac: AsyncClient):
    response = await ac.post(
        "/users/",
        json={
            "username": "test_user",
            "surname": "test_surname",
            "email": "test@gmail.com",
            "hashed_password": "12345Test",
        },
    )
    print(response)
