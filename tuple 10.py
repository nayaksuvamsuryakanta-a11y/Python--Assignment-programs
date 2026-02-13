t = (-1, 2, -3, 4)
new_t = ()

for num in t:
    if num > 0:
        new_t += (num,)

print(new_t)