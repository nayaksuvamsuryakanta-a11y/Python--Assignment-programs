t = (10, 20, 30, 40, 50)
even_pos = ()

for i in range(len(t)):
    if i % 2 == 0:
        even_pos += (t[i],)

print(even_pos)