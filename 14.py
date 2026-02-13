lst = [1, 2, 2, 3, 3, 3]
freq = {}

for num in lst:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)