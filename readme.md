# Error handler decorators

This project contains decorators for handling errors

### Base error handler

Surrounds the function with a try catch, and in case of an exception, prints the functions name, its module and the raised error.
Is used by adding the decorator above the function you want to handle.
```
@handle_error
def a_function(a, b):
```