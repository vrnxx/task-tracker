from typing import Annotated

from fastapi import APIRouter, Depends

from src.api.dependencies import user_service
from src.models.dto.user import UserDto
from src.schemas.user_schema import UserAddSchema
from src.services.user_service import UserService

router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/{user_id}')
async def get_user(user_id: int, user_service:
                   Annotated[UserService, Depends(user_service)]
                   ) -> UserDto:
    user = await user_service.get_user_by_id(user_id)
    return user


@router.get('/')
async def get_users(
        user_service: Annotated[UserService, Depends(user_service)]
) -> list[UserDto]:
    users = await user_service.get_all_users()
    return users


@router.post('/')
async def add_user(user_data: UserAddSchema,
                   user_service: Annotated[UserService, Depends(user_service)]
                   ) -> UserDto:
    added_user = await user_service.add_user(user_data)
    return added_user

