n = int(input("Enter a number: "))
d = {}

for i in range(1, n + 1):
    d[i] = i * i

print("Dictionary of squares:", d)