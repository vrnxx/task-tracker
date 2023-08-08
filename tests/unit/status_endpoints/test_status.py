from httpx import AsyncClient


async def test_get_status_by_id(ac: AsyncClient):
    status_id = "1"
    response = await ac.get(url="/status/" + status_id)

    print(
        f"status_by_id: {response.json()}"
    )  # {'id': 1, 'title': 'test_open_status'}


async def test_get_all_statuses(ac: AsyncClient):
    response = await ac.get(url="/status/")

    data = response.json()

    assert data == [{"id": 1, "title": "test_open_status"}]
