d = {"A": 10, "B": 20, "C": 30}
key = input("Enter key to delete: ")

if key in d:
    del d[key]
    print("Key deleted successfully")
else:
    print("Key not found")

print("Updated dictionary:", d)