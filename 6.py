lst = [1, 2, 3, 4]
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Reversed list:", rev)