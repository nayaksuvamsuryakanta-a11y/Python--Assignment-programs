t = (1, 2, 3, 4, 5)
even = odd = 0

for num in t:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)