lst = [10, 20, 4, 45, 99]
largest = second = -999999

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest:", second)