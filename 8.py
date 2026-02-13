lst = [1, 2, 2, 3, 4, 4]
unique = []

for num in lst:
    if num not in unique:
        unique.append(num)

print("Without duplicates:", unique)