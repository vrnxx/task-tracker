from pydantic import BaseModel


class UserAddSchema(BaseModel):
    username: str
    surname: str
    email: str
    hashed_password: str

