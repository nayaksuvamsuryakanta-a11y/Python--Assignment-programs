lst = [10, 20, 30, 40, 50]

even_index = []
odd_index = []

for i in range(len(lst)):
    if i % 2 == 0:
        even_index.append(lst[i])
    else:
        odd_index.append(lst[i])

print("Even index:", even_index)
print("Odd index:", odd_index)