from fastapi import APIRouter, Depends
from typing import Annotated
from src.api.dependencies import user_service
from src.services.user_service import UserService
from src.schemas.user_schema import UserAddSchema, UserSchema


router = APIRouter(
    prefix='/users',
    tags=['users'],
)


@router.get('/{user_id}', response_model=UserSchema)
async def get_user(user_id: int, user_service:
                   Annotated[UserService, Depends(user_service)]):
    user = await user_service.get_user_by_id(user_id)
    return user


@router.get('/', response_model=list[UserSchema])
async def get_users(user_service:
Annotated[UserService, Depends(user_service)]):
    users = await user_service.get_all_users()
    return users


@router.post('/')
async def add_user(user_data: UserAddSchema,
                   user_service: Annotated[UserService, Depends(user_service)]) -> UserSchema:
    added_user = await user_service.add_user(user_data)
    return added_user

