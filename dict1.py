n = int(input("Enter number of students: "))
students = {}
count = 0

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

for marks in students.values():
    if marks >= 40:
        count += 1

print("Number of students with marks ≥ 40:", count)