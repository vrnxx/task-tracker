from abc import ABC, abstractmethod


class AbstractDAO(ABC):
    """
    Interface for all DAOs.

    If you want to implement your own DAO,
    you need to inherit from this class and set a model attribute
    to you model class.
    """

    model = None

    @abstractmethod
    async def add_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update_one(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete_one(self, *args, **kwargs):
        raise NotImplementedError
