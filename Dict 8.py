d = {"A": 10, "B": 50, "C": 30}

max_key = None
max_value = -999999

for key in d:
    if d[key] > max_value:
        max_value = d[key]
        max_key = key

print("Key with maximum value:", max_key)