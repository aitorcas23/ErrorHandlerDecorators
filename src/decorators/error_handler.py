"""Decorators for error handling."""
import os
import inspect


def handle_error(func):
    """Wrap a function with a try-except block to handle any exceptions raised.

    This decorator prints the error message, the name of the function that raised the exception, and the name of the
    module where the function is defined. This can be useful for debugging and logging purposes.

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
            print(f'{e} {procedure} {module}')
    return add_try_catch
