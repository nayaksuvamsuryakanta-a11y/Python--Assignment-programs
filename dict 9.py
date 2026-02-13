d1 = {"A": 10, "B": 20}
d2 = {"C": 30, "D": 40}

merged = {}

# Add elements of first dictionary
for key in d1:
    merged[key] = d1[key]

# Add elements of second dictionary
for key in d2:
    merged[key] = d2[key]

print("Merged Dictionary:", merged)