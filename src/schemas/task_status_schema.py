from pydantic import BaseModel


class TaskStatusSchema(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class TaskStatusAddSchema(BaseModel):
    title: str
