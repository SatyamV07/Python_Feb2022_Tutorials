# Json Module

data = {
    "firstName": "Maximum",
    "secondName": "Minumum",
    "hobbies": ["Jogging", "sky diving", "XBOX"],
    "age": 70,
    "children": [{"firstname": "Alice", "age": 20}, {"firstname": "Steve", "age": 22}],
}

import json

# Method 1 and should not use instead we can with context managers
# to solve the file close problem
# file_one = open(r"C:\Users\kramalinga23\Desktop\test.txt", "w")
# file_one.write("Hello there")
# file_one.close()

# With Context managers

with open(r"C:\Users\kramalinga23\Desktop\data_file.json", "w") as write_file:
    json.dump(data, write_file)

with open(r"C:\Users\kramalinga23\Desktop\data_file.json", "r") as read_file:
    json_data = json.load(read_file)

print(json_data)

print()

import csv

with open(r"C:\Users\kramalinga23\Desktop\employee_birthday.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column Names are {', '.join(row)}")
            line_count += 1
        else:
            print(
                f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}."
            )
            line_count += 1
        print(f"Processes {line_count} lines")

print()

import pandas

df = pandas.read_csv(r"C:\Users\kramalinga23\Desktop\hrdata.csv")
print(df)
print()

# df = pandas.read_csv(r"C:\Users\kramalinga23\Desktop\hrdata.csv", index_col="Name")
# print(df)

print(type(df["Name"]))
print(list(df["Name"]))
