# For Loop - Actual Mechanism

L1 = []

for value in range(5):
    L1.append(value)

print("Using Traditional Method", L1)

print()
# List comprehension

L1 = [value for value in range(5)]
print("Using List comprehension Method", L1)

# [element for element in <iterable] <if condition>]

print()

# L1 = [value if value % 10 == 0 else value + 1 for value in range(1000)]
L1 = [value for value in range(1000) if value % 10 == 0]
print(L1)

print()

fruits = ["apple", "orange", "jackfruit", "grapes", "banana", "lime"]
modified_fruits = [
    fruit.title() if len(fruit) == 6 else fruit.upper() for fruit in fruits
]
print(modified_fruits)

# [(if condition satisfies output) if condition else (else condition satisfies output) for <element> in <iterable>]

print()

# Set Comprehension

modified_fruits = {
    fruit.title() if len(fruit) == 6 else fruit.upper() for fruit in fruits
}
print(modified_fruits)


# Dictionary Comprehension

print()

KEY = ["Name", "Voter_ID", "PAN_ID"]
VALUE = ["XYZ", "WQUXIU789", "BBBBBBB"]

d1 = {key: value for key, value in zip(KEY, VALUE)}
print(d1)

print()
# Tuple Comprehension

modified_fruits = (
    fruit.title() if len(fruit) == 6 else fruit.upper() for fruit in fruits
)
print(modified_fruits)
