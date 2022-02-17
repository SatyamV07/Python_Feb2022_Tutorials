import math

L1 = [
    1,
    2.0,
    3 - 78j,
    2.34e-78,
    math.pi,
    2,
    2,
    4,
    bin(546738),
    hex(120),
    oct(56),
    [78, 34, 21],
    (100, 200),
    "apple",
    "c",
    "Z",
    {89, 1000, "HBO"},
    dict(a=121, b=200),
    18,
    18,
    [1, 2, 3],
    [1, 2, 3],
]

print(
    """
Thse are the methods available for list class under L1 variable, also these 
L1 Methods would be the same as dir(list) as L1 have list class
"""
)

print("=" * 70)

print(dir(L1))
print()

print(f"{L1 = }")
print()
L1.append(f"{len(L1) = }")  # append will add only one element at the end of the list
print(f"L1.append(len(L1) = {L1}")
print()
L1.append(10_000)
print(f"L1.append(10_000) = {L1}")
print()
L1.extend((10, 1000))  # extend will add one ore more element at the end of the list
print(f"L1.extend((10, 1000)) = {L1}")
print()
print(f"{L1.count([1,2,3]) = }")
print()
print(f"{L1.index([1, 2, 3]) = }")
print()
L1.insert(8, ("Hi", "there"))
print(f'L1.insert(8, ("Hi", "there")) = {L1}')

L1[8] = 20  # This is override the element with new element
print()
print(f"{L1 = }")
print()
L1.pop()
print(f"L1.pop() = {L1}")
print()
L1.pop(0)
print(
    f"L1.pop(0) = {L1}"
)  # Mention the index number inside pop() to remove particular element
print()
L1.remove([1, 2, 3])
print(f"L1.remove([1, 2, 3]) = {L1}")
print()
L1.reverse()
print(f"L1.reverse() = {L1}")
print()
L2 = L1.copy()
print(f"L1.copy() = L2 = {L2}")

print()

print("=" * 70)
print(f"final L1 = {L1}")
print()
print(f"final L2 = {L2}")
print("=" * 70)

print()
L1.clear()
print(f"Finally clearing my list L1.clear() = {L1}")
