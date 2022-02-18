# Set Methods

print(
    """
These are the methods available for set class under a,b,c,d variables, 
also these set(a,b,c,d) methods would be the same as dir(set) as above variables have set dtype"""
)

print("=" * 90)

a = set(range(1, 6))  # {1, 2, 3, 4, 5}
b = set(range(3, 8))  # {3, 4, 5, 6, 7}
c = set(range(5, 10))  # {5, 6, 7, 8, 9}
d = set(range(7, 12))  # {7, 8, 9, 10, 11}
print(dir(set) == dir(a))
print(dir(a))
print("=" * 90)

print()

# Union of
print(f"{a.union(b) = }")
print(f"{a.union(b,c,d) = }")
print(f"{a.union([100, 200, 300]) = }")
print(f"{a.union([100, 200, 300], [400, 500, 600]) = }")
print(f"{a.union(dict(apple='red')) = }")
print(f"same of a.union(b) = {a | b = }")
print(f"same of a.union(b,c,d) = {a | b | c | d = }")

print()

# Intersection of
print(f"{a.intersection(b) = }")
print(f"{a.intersection(b,c,d) = }")
print(f"same of a.intersection(b) = {a & b = }")
print(f"same of a.intersection(b,c,d) = {a & b & c & d = }")

print()

# Difference of
print(
    "Difference of multiple sets is the set of only the elements"
    "that exist in the first set but not in any of the rest"
)
print(f"{a.difference(b) = }")
print(f"{a.difference(b, c,d) = }")
print(f"same of a.difference(b) = {a - b = }")
print(f"same of a.difference(b) = {a - b - c - d = }")
print(f"same of a.difference(b) = {b - a = }")
print(f"same of a.difference(b) = {b - a - c - d = }")

print()

x1 = set("foo bar baz".split())
print(f"{x1 = }")
x1.add("boss")
print(f"x1.add('boss') = {x1 = }")


print()
x1.remove("bar")
print(f"x1.remove('bar') = {x1 = }")


print()
x1.discard("false")
print(f"x1.discard('false') = {x1 = }")

print()
d = {100, 673, 400, 1000, 2, 0, "apple"}
print(f"{d = }")
d.pop()
print(f"d is now after the pop method {d = }")
d.pop()
print(f"d is now after the pop method {d = }")
d.pop()
print(f"d is now after the pop method {d = }")
d.pop()
print(f"d is now after the pop method {d = }")
d.pop()
print(f"d is now after the pop method {d = }")


# problem in adding element in set

# d.add([1, 2, 3, 4, 5])
# d.add(dict(a=20, b=30))
d.add("1")
print(f"{d = }")
d.add(100000000)
print(f"{d = }")
d.add((89,))
print(f"{d = }")
