d = {"A": 30, "B": 10, "C": 20}

# Convert dictionary to list of items
items = list(d.items())

# Bubble sort based on values
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:
            items[i], items[j] = items[j], items[i]

# Convert back to dictionary
sorted_dict = dict(items)

print("Dictionary sorted by values:", sorted_dict)