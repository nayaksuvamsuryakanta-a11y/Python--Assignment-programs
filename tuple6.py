t = (5, 2, 9, 1)
maxi = mini = t[0]

for num in t:
    if num > maxi:
        maxi = num
    if num < mini:
        mini = num

print("Max:", maxi)
print("Min:", mini)