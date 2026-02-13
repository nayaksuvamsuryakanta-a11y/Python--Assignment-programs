lst = [5, 2, 9, 1, 7]
largest = smallest = lst[0]

for num in lst:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)