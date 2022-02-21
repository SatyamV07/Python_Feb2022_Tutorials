print("\n")

# Functions without arguments


def greet_print():  # Line 6 to 8 is function definition
    """Functions without arguments"""
    print("Hellooooo World!")


greet_print()


def greet_return():  # Line 6 to 8 is function definition
    """Functions without arguments"""
    return "Hellooooo World!"


print(greet_return())


# Functions with arguments


def power_of_two(number: int) -> int:  # number is a positional argument
    """This function is used to get the power of 2 with the value of number"""
    return pow(number, 2)


print(power_of_two(20))


# Functions with multiple positional arguments


def name_of_the_person(fname: str, lname: str) -> str:
    """This function is used to get the last and first name of a person"""
    print("Hello")
    print(f"{id(lname) = }")
    print(f"{id(fname) = }")
    return lname.upper(), fname.upper()


print(name_of_the_person("Kumaran", "Ramalingam"))

LNAME, FNAME = name_of_the_person("Kumaran", "Ramalingam")

print(f"{id(LNAME) = }")
print(f"{id(FNAME) = }")


print()
# Default arguments function

from math import pi


def area_of_circle(radius=10):
    """This function is used to get the area_of_circle"""
    return pi * (radius ** 2)


print("Area of the circle is: %.2f" % area_of_circle())

# Positional arguments function


def normal_arguments_function(x: int, y: int, z: str, a: float, b: int, c: int):
    """normal_arguments_function"""
    return x ** 2, y / 200, z.upper(), a, b, c


print(normal_arguments_function(10, 20, "thirty", 40.67, 50, 60))


def positional_arguments_function(*args):
    """normal_arguments_function"""
    return [arg for arg in args]


print(positional_arguments_function(10, 20, "thirty", 40.67, 50, 60))


# Keyword Argument Function


def keyword_arguments_function(**kwargs):
    """keyword_arguments_function"""
    data = kwargs
    return data.values()


print(keyword_arguments_function(name="Kumaran", exp=12))


# Mix of all arguments type


def default_positional_keyword_argument_function(city="xyz", *args, **kwargs):
    """Mix of all above types of arguments"""
    print(city)
    print(args)
    print(kwargs)


d1 = dict(degree=32.7, Fahrenheit=40)
default_positional_keyword_argument_function("Nagaland", 20, 21.5, **d1)
