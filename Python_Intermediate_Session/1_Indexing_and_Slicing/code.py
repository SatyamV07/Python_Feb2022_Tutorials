print("===================================================")
L1 = "spam ham egg bacon spring boot".split()
print(L1)
print("===================================================")


# Indexing

print(f"{L1[3] = }")  # Forward indexing
print(f"{L1[-2] = }")  # Reverse indexing
print(f"{L1[4] = }")  # Forward indexing
print(f"{L1[2] = }")  # Forward indexing
print(f"{L1[-6] = }")  # Reverse indexing
print(f"{L1[0] = }")  # Forward indexing


print()

# Forward Index Slicing

# L1[start: stop: step]

print(f"{L1[0:1] = }")
print(f"{L1[0:2] = }")
print(f"{L1[0:3] = }")
print(f"{L1[0:4] = }")
print(f"{L1[0:5] = }")
print(f"{L1[0:6] = }")
print(f"{L1[0:7] = }")
print(f"{L1[0:] = }")
print(f"{L1[:] = }")
print(f"{L1[::] = }")

print()


# Forward listing with negative Index

# L1[start: stop: step]

print(f"{L1[-6:] = }")
print(f"{L1[-6:-1] = }")
print(f"{L1[-6:-2] = }")
print(f"{L1[-6:-3] = }")
print(f"{L1[-6:-4] = }")
print(f"{L1[-6:-5] = }")

print()

# Reverse listing with negative index and -1 step value

print(f"{L1[-1:-2:-1] = }")
print(f"{L1[-1:-3:-1] = }")
print(f"{L1[-1:-4:-1] = }")
print(f"{L1[-1:-5:-1] = }")
print(f"{L1[-1:-6:-1] = }")
print(f"{L1[-3:-6:-1] = }")
print(f"{L1[-1:-6:-2] = }")
print(f"{L1[-1:-6:-3] = }")

print()

# Reverse listing with negative index

print(f"{L1[-6::-1] = }")
print(f"{L1[-5:-7:-1] = }")
print(f"{L1[-4:-6:-1] = }")
print(f"{L1[-3:-5:-1] = }")
print(f"{L1[-2::-1] = }")
print(f"{L1[-1::-1] = }")

print()

# Forward listing using step values

print(f"{L1[::2] = }")
print(f"{L1[1::2] = }")
print(f"{L1[3::2] = }")

print()

# Reverse Listing using step values

print(f"{L1[::-1] = }")
print(f"{L1[::-2] = }")
print(f"{L1[-3::-2] = }")

print()


T1 = tuple(L1)
S1 = set(L1)

print("Tuple Indexing")
print(f"{T1[::-1] = }")

print()

print("Set Indexing")
print(L1)
print(S1)
print(S1[0])
