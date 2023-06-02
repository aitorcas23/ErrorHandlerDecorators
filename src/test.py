from decorators import error_handlers, timers
from time import sleep
import logging


@timers.default_timer
def a_function(a: int, b: int):
    return (a / b)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    print(a_function(1, 2))
