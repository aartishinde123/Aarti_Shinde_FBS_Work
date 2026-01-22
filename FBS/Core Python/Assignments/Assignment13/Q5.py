# Python Program to Sum All the Items in a Dictionary

data = {"x": 5, "y": 15, "z": 25}

total = 0

for value in data.values():
    total += value

print("Sum:", total)
