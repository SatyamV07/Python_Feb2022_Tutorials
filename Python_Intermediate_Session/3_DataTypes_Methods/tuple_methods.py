import math

T1 = (
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
)


print(
    """
Thse are the methods available for tuple class under T1 variable, also these 
T1 Methods would be the same as dir(tuple) as T1 have tuple class.
"""
)

print("=" * 70)

print(dir(T1))
print()
print(f"{T1 =}")
print()
print(f"{T1.count(18) = }")
print()

print(f'{T1.index({1000, 89, "HBO"}) = }')
