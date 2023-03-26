from typing import Callable, Literal
import os

from func_attributes import code_to_value


COLORS = {"Info": "", "Warning": '\033[93m', "Error": '\033[91m'}
END = '\033[0m'


def custom_error_handler(format: list | tuple, color: Literal["Info", "Warning", "Error"] = "Info"):
    def handle_error(func: Callable):
        def add_try_catch(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                message = COLORS[color]
                for value in format:
                    if not isinstance(value, str):
                        value = code_to_value[value](e)
                    message += str(value)
                return message + END
        return add_try_catch
    return handle_error


def default_error_handler(func):
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
        try:
            return func(*args, **kwargs)
        except Exception as e:
            procedure = e.__traceback__.tb_next.tb_frame.f_code.co_name
            module = os.path.basename(e.__traceback__.tb_next.tb_frame.f_code.co_filename).split(".")[0]
            line = e.__traceback__.tb_next.tb_lineno
            print(f"""{COLORS['Warning']}An error occurred in line {line} in procedure {procedure} in module {module}:
{e}{END}""")
    return add_try_catch
