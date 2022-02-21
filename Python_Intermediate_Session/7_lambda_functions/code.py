exec1 = lambda x: x + 200
print(exec1(2))
print((lambda x: x + 200)(2))
print((lambda x, y, z: x + y * z)(1, 2, 3))
print((lambda x, y, z=200: x + y * z)(1, 2))
print((lambda *args: sum(args))(1, 2, 3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))


# map() and filter()

print()
print(list(map(lambda x: x.upper(), ["cat", "cow", "lamb"])))
print(list(filter(lambda x: "o" in x, ["cat", "cow", "lamb"])))
print([anim for anim in ["cat", "cow", "lamb"] if "o" in anim])

# Complex lambda functions

print(
    (lambda some_list: list(map(lambda n: n // 2, some_list)))(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    )
)


def div_times(some_list):
    div_by_two = lambda n: n // 2
    return list(map(div_by_two, some_list))


print()

print(div_times([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print()


ids = "id1 id30 id2 id22 id100".split()
print(sorted(ids))  # Lexicographic sort

print(sorted(ids, key=lambda x: int(x[2:]), reverse=False))
