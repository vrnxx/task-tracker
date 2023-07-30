from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


class UserAddSchema(BaseModel):
    username: str
    email: str
    hashed_password: str

