from pydantic import BaseModel


class UserAddSchema(BaseModel):
    username: str
    email: str
    hashed_password: str

