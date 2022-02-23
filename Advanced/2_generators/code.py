L1 = "apple orange soda lime".split()
t1 = 7, 8, 9, 10, 11, 12
s1 = {87, "Pomogranete", 3 + 3j}
d1 = dict(a=77, b=88, c="Goa")

for value in L1:
    print(value)

print()

for value in t1:
    print(value)

print()

for value in s1:
    print(value)

print()

for key, value in d1.items():
    print(key, value)

print()

print([value for value in L1])  # List comprehension
print({value for value in s1})  # Set Comprehension
print({key: value for key, value in d1.items()})  # Dictionary Comprehension
print((value for value in t1))  # Generators
print()

# This is a Generator Expression

generator = (i ** 2 for i in range(10))

for _ in range(5):
    print(next(generator))

for _ in range(5):
    print(next(generator))

# for _ in range(10):
#     print(next(generator))

print()
# This is a Generator Function


def normal_function():
    for x in range(10):
        print(x ** 2)


normal_function()

print()


def generator_function():
    for x in range(10):
        yield x ** 2


print(generator_function())
g1 = generator_function()

for x in range(5):
    print(next(g1))


def multi_yield():
    yield_str = "This wil print the first string"
    yield yield_str
    yield_str = "This wil print the second string"
    yield yield_str


print()
multi_obj = multi_yield()
print(next(multi_obj))
print(next(multi_obj))
