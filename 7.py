lst = [-1, 2, -3, 4, 5]
pos = []
neg = []

for num in lst:
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

print("Positive:", pos)
print("Negative:", neg)