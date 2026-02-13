t1 = (1, 2, 3, 4)
t2 = (3, 4, 5)

common = ()

for num in t1:
    if num in t2 and num not in common:
        common += (num,)

print(common)