from typing import Callable
from os import path
from inspect import getfile


class BaseHandler():
    error: Exception

    def __init__(self, func: Callable) -> None:
        self.name = func.__name__
        self.file_name = path.basename(getfile(func)).split('.')[0]

    def error_message(self):
        return f"""An error occurred in procedure {self.name} in module {self.file_name}:
        {self.error}"""
