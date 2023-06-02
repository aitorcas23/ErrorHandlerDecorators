"""Timer decorators."""

from time import time
from typing import Callable, TypeVar, ParamSpec
import logging

T = TypeVar("T")
P = ParamSpec("P")


def default_timer(func: Callable[P, T]) -> Callable[P, T]:
    """Decorate a function with this to time the execution of the function."""
    def add_timer(*args: P.args, **kwargs: P.kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        logging.info(f"{func.__name__} took {round(end - start, 2)} seconds to execute")
        return result
    return add_timer
