from pydantic import BaseModel


class StatusSchema(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class StatusAddSchema(BaseModel):
    title: str
