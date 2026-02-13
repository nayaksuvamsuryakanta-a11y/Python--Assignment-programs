lst = [1, 2, 3, 4, 5]
k = 2

rotated = lst[k:] + lst[:k]
print("Rotated List:", rotated)