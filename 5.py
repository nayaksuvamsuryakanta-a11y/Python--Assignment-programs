lst = [1, 2, 2, 3, 2, 4]
x = int(input("Enter element to count: "))
count = 0

for num in lst:
    if num == x:
        count += 1

print("Count:", count)