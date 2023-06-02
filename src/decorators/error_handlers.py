"""Error handling decorators."""
import os
from typing import Callable, TypeVar, ParamSpec
import logging

COLORS = {"Info": "", "Warning": '\033[93m', "Error": '\033[91m'}
END = '\033[0m'

T = TypeVar('T')
P = ParamSpec("P")


def default_error_handler(func: Callable[P, T]) -> Callable[P, T]:
    """Wrap a function with a try-except block to handle any exceptions raised.

    This decorator prints the error message, the name of the module where the function is defined,
    the name of the function that raised the exception, and the line where the exception was raised.
    This can be useful for debugging and logging purposes.

    Example:
        ```
        @default_error_handler
        def some_function():
        ```
    """
    def add_try_catch(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            traceback = e.__traceback__
            if traceback is None:
                raise e

            tb_next = traceback.tb_next
            if tb_next is None:
                raise e

            procedure = tb_next.tb_frame.f_code.co_name
            module = os.path.basename(tb_next.tb_frame.f_code.co_filename).split(".")[0]
            line = tb_next.tb_lineno
            logging.error(f"""An error occurred in line {line} in procedure {procedure} in module {module}:
{type(e).__name__}: {e}""")
            
            raise e
    return add_try_catch
