# Inner Functions


from email import message
import string
from tracemalloc import start
from unicodedata import name


# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     inner_func()


# outer_func("Hello")

# Function Closures


# def outer_func(msg):
#     message = msg

#     def inner_func(newmsg):
#         print(" ".join((message, newmsg)))

#     return inner_func


# new_func = outer_func("Hello")
# new_func("there")

# Decorator Function


def my_decorator(func):  # 'func' is say_hello function
    def wrapper():
        print("Something executed before the function called")
        func()  # say_hello is executed
        print("Something executed after the function called")

    return wrapper


@my_decorator
def say_hello():
    print("Hello I was asked to be decorated")


say_hello()

# say_hello_closure = my_decorator(say_hello)
# say_hello_closure()

print()

# Decorator 2


# def do_twice(func):
#     def wrapper_do_twice():
#         string1 = func()
#         print(string1.upper())
#         print(func())

#     return wrapper_do_twice


# @do_twice
# def do_twice_say_hello():
#     return "Hello"


# do_twice_say_hello()

# Decorator 3

from functools import wraps


def do_twice(func):
    @wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


@do_twice
def greet(*args, **kwargs):
    print("Creating Greeting")
    print(f"Hi {args[0]} I won't {args[1]}")
    print(kwargs)


greet("Kumaran", "say", hobby="space studies")
print(greet.__name__)

# Boilerplate template


def decorated_function(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapped_function


print()

# Example for Decorator

import time


def timer(func):
    """Print the runtime of the decorated function"""

    @wraps(func)
    def wrapper_time(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_time


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])
    else:
        return "Loop Finished"


print(waste_some_time(2000))
print(waste_some_time.__name__)

print()

# Execution of another file repeater.py

from repeater import repeat


@repeat(num_times=3)
@do_twice
@do_twice
def repeat_greet(name):
    print(f"Hello {name}")


repeat_greet("Friends")
print(repeat_greet.__name__)
