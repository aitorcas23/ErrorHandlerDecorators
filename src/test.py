from decorators.base_error_handler import handle_error


@handle_error
def a_function(a, b):
    return (a / b)


if __name__ == "__main__":
    print(a_function(1, 2))
    print(a_function(5, 0))
