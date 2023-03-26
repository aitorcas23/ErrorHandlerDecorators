"""Decorators for error handling."""
import os
import inspect


ERROR = '\033[91m'
ENDC = '\033[0m'


def handle_error(func):
    """Wrap a function with a try-except block to handle any exceptions raised.

    This decorator prints the error message, the name of the module where the function is defined,
    the name of the function that raised the exception, and the line where the exception was raised.
    This can be useful for debugging and logging purposes.

    Example:
    ```
    @handle_error
    def some_function():
    ```
    """
    def add_try_catch(*args, **kwargs):
        procedure = func.__name__
        module = os.path.basename(inspect.getfile(func)).split(".")[0]
        try:
            return func(*args, **kwargs)
        except Exception as e:
            line = e.__traceback__.tb_next.tb_lineno
            print(f"""{ERROR}An error occurred in line {line} in procedure {procedure} in module {module}:
{e}{ENDC}""")
    return add_try_catch
