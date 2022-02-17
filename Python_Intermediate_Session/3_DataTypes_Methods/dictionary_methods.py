hollywood_movies = {
    "Marvel": "Avengers",
    "Disney": "Dumbo",
    "Universal Studios": "FF9",
    "Fox Studios": "Avatar",
    "Pixar Studios": "Cars",
    "Warner Bros": "Inception",
}
print(
    """
These are the methods available for dict class under 
hollywood_movies variable, also these hollywood_movies methods would be 
the same as dir(dict) as hollywood_movies have dict data type"""
)
print("======================================================")
print(dir(hollywood_movies))
print("\n")
print(hollywood_movies["Disney"])
print()
print(hollywood_movies.get("Disney"))
print()
print(hollywood_movies.items())
print()
print(hollywood_movies.keys())
print()
print(hollywood_movies.values())
print()
hollywood_movies.pop("Warner Bros")
print(hollywood_movies)
hollywood_movies.popitem()
print()
print(hollywood_movies)
# hollywood_movies.pop("Syncopy")
print("Avengers" in hollywood_movies)
print()
for company, movies in hollywood_movies.items():
    print(company)
    print(movies)

print()
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 10, "d": 100, "e": 7}
print(f"{d1 = }")
print(f"{d2 = }")

d1.update(k=20)
print(f"{d1 = }")
d1["z"] = 3+4j
print(f"{d1 = }")

d1.update(d2)
print(f"{d1 = }")


d3 = {"data1":  {"Name": "xyz"}}
print(f"{d3 = }")
print(d3.get("data1").get("Name"))
print(d3["data1"]["Name"])
print(d1|d2)
d4 = d1 |d3 | dict(apple="red")
print(d4)

d1.update(dict(orange="orange"))
print(f"{d1 = }")

d3 = {"name": "xyz"}
print({**d1, **d2, **d3})
