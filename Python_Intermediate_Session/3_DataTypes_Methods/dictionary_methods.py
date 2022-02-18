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
hollywood_movies variable, also these hollywood_movies 
methods would be the same as dir(dict) as 
hollywood_movies have dict data type"""
)
print("=" * 90)

print(dir(hollywood_movies))
print("=" * 90)
print()
print(f"{hollywood_movies['Disney'] = }")
print(f"{hollywood_movies.get('Disney') = }")
print()
print(f"{hollywood_movies.items() = }")
print()
print(f"{hollywood_movies.keys() = }")
print()
print(f"{hollywood_movies.values() = }")
print()
hollywood_movies.pop("Pixar Studios")
print(f"hollywood_movies.pop('Pixar Studios') = {hollywood_movies = }")
print()
hollywood_movies.popitem()
print(f"hollywood_movies.popitem() = {hollywood_movies = }")
# hollywood_movies.pop("Syncopy") # Will through KeyError: 'Syncopy' if key is not there
print()
print("Avengers" in hollywood_movies)
print()

for company, movies in hollywood_movies.items():
    print(company, movies)

print()

d1 = dict(a=1, b=2, c=3)
d2 = dict(b=10, d=100, e=7)
print(f"{d1 = }")
print(f"{d2 = }")

d1.update(k=20)
print(f"{d1 = }")
d1["z"] = 3 + 4j
print(f"{d1 = }")

d1.update(d2)
print(f"{d1 = }")

d3 = {"name": "xyz"}
print({**d1, **d2, **d3})
