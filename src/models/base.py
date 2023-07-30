from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, registry

meta = MetaData()


class Base(DeclarativeBase):
    reg = registry()
