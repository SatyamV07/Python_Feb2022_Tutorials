print("\n")


def outer_function():
    message = "Hello"

    def inner_function():
        print(message)

    inner_function()


outer_function()
# print(inner_function())
print()


def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func


new_outer_func = outer_func("outer_function")
new_outer_func()

print()


def generate_power(exponent):
    def power(base):
        return base ** exponent

    return power


raise_two = generate_power(2)
raise_three = generate_power(3)
raise_four = generate_power(4)

print(raise_two(30))
print(raise_three(100))
print(raise_four(100))
