from functools import wraps
from typing import Any, Callable, Coroutine, ParamSpec, TypeVar

from src.utils.exceptions import exceptions

Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")
Func = Callable[Param, ReturnType]


def task_exception_mapper(
        func: Callable[Param, Coroutine[Any, Any, ReturnType]]
) -> Callable[Param, Coroutine[Any, Any, ReturnType]]:
    @wraps(func)
    async def wrapped(*args: Param.args, **kwargs: Param.kwargs) -> ReturnType:
        try:
            return await func(*args, **kwargs)
        except AttributeError:
            raise exceptions.TaskNotFoundError

    return wrapped


def status_exception_mapper(
        func: Callable[Param, Coroutine[Any, Any, ReturnType]]
) -> Callable[Param, Coroutine[Any, Any, ReturnType]]:
    @wraps(func)
    async def wrapped(*args: Param.args, **kwargs: Param.kwargs) -> ReturnType:
        try:
            return await func(*args, **kwargs)
        except AttributeError:
            raise exceptions.StatusNotFoundError

    return wrapped
