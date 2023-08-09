from httpx import AsyncClient


async def test_get_status_by_id(ac: AsyncClient):
    status_id = 1
    response = await ac.get(url=f"/status/{status_id}")

    data = response.json()

    assert response.status_code == 200
    assert data == {"id": 1, "title": "test_open_status"}


async def test_get_all_statuses(ac: AsyncClient):
    response = await ac.get(url="/status/")

    data = response.json()

    assert data == [{"id": 1, "title": "test_open_status"}]
