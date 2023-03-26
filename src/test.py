from func_attributes import FuncAttributes
from decorators.error_handlers import custom_error_handler


format = ["An error occurred in line ",
          FuncAttributes.line,
          " in procedure ",
          FuncAttributes.name,
          " in module ",
          FuncAttributes.module,
          ":\n",
          FuncAttributes.error]


@custom_error_handler(format=format, color="Error")
def a_function(a, b):
    return (a / b)


if __name__ == "__main__":
    print(a_function(1, 2))
    print(a_function(5, 0))
