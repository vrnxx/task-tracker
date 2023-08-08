from httpx import AsyncClient


async def test_add_status(ac: AsyncClient):
    response = await ac.post(
        "/status/",
        json={
            "title": "test_open_status",
        },
    )
    data = response.json()

    assert response.status_code == 201, "Response status code must be 201"
    assert data["id"] == 1, "Incorrect id from response data"
    assert (
        data["title"] == "test_open_status"
    ), "Incorrect title from response data"


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
    data = response.json()

    assert response.status_code == 201, "Response status code must be 201"
    assert data["id"] == 1, "Incorrect response data"
    assert (
        data["username"] == "test_user"
    ), "Incorrect username from response data"
    assert (
        data["surname"] == "test_surname"
    ), "Incorrect surname from response data"
    assert (
        data["email"] == "test@gmail.com"
    ), "Incorrect email from response data"
