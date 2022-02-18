# 1 "Old School Style" String Formatting (% Operator)

name = "Kumaran"
errno = 674666525526

# print("Hello," + " " + name)

# print("Hello, %s" % name)

# print("%x" % errno)

# print("Hey %s, there is a 0x%x error" % (name, errno))

# print("This is a decimal or integer %d" % 89.67)

# print("This is a floating point number %.4f" % 89.345678)

# print("This is a exponent %e" % 24.67)

# print("This is a exponent %E" % 24)

# print("This is a exponent %c" % "A")

# print("This is a string %r" % "representation")

# print("This is an ASCII representation of %a" % "a")


# ==================================================================================

print(type(str()))

string_1 = "foo bar baz jaaz bazz"
string_2 = "63728283833"
string_3 = "    first line  second line  "
string_4 = "0"
print(
    """
These are the methods available for string class under string_1 variable, also these 
string_1 variable methods would be the same as dir(str) as string_1 have str date type
"""
)
print("=" * 90)

print(dir(string_1))

print("=" * 90)
print()

print(f"{string_1.upper() = }")
print(f"{string_1.lower() = }")
print(f"{string_1.title() = }")
print(f"{string_1.capitalize() = }")
print(f"{string_1.startswith('foo ') = }")
print(f"{string_1.endswith('-bazz') = }")
print(f"{string_1.endswith('az ') = }")
print(f"{string_1.endswith('bazz ') = }")
print(f"{string_1.count('ba') = }")
print(f"{string_1.count('az') = }")
print(f"{string_1.split() = }")
print(f"{string_4.split('.') = }")
print(f"{string_3.strip() = }")
print(f"{string_3.split()[0].isalpha() = }")
print(f"{string_4.isdigit() = }")
print(f"{string_4.isdecimal() = }")
print(f"{string_1.index('jaaz') = }")
print(f"{string_1.find('bazz', 10, 15) = }")
print(f"{string_1.replace('foo', 'zoo') = }")
print(f"{string_1.partition('a') = }")
print(" ".join((string_1, string_2)))


# 2 "New Style" String Formatting (str.format)

print("Name is {}".format(name))
print("Name is {0} and the error code is {1}".format(name, errno))
print(
    "Name is {named} and the error code is {errno} and this is {} and may be {} later".format(
        "critical", "fatal", named=name, errno=errno
    )
)


# ==================================================================================

print(string_1 + " " + string_2)  # This is string concatenation
print(string_1 * 2)  # String Multiplication


# 3 "F String Formatting"

print(f"Hello, {name}")
print(f"Addition of two number {1 + 2}")
a = 20
b = 22
print(f"is 'a' is greater than 'b' {a > b}")
print(f"Binary number representation of 95 is {bin(95)}")
print(f"{string_1.count('ba') = }")  # Always carefull on handling with quotes
