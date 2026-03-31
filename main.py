from models import Student, Admin
from storage import load_data, save_data
from utils import get_int, get_non_empty_string

# Hardcoded admin for demonstration
ADMIN = Admin("admin", "password123")


def authenticate():
    print("--- Admin Login ---")
    user = input("Username: ")
    pwd = input("Password: ")
    if user == ADMIN.username and ADMIN.verify(pwd):
        return True
    print("Invalid credentials.")
    return False


def add_student():
    try:
        roll = get_non_empty_string("Roll No: ")
        name = get_non_empty_string("Name: ")
        marks = get_int("Marks: ")
        data = load_data()
        # Check duplicate
        if any(s['roll_no'] == roll for s in data):
            print("Roll No exists.")
            return
        data.append(Student(roll, name, marks).to_dict())
        save_data(data)
        print("Student added.")
    except Exception as e:
        print(f"Error: {e}")


def search_student():
    term = input("Search Name or Roll: ").lower()
    data = load_data()
    results = [s for s in data if term in s['name'].lower() or term in s['roll_no'].lower()]
    if results:
        for s in results: print(f"{s['roll_no']} - {s['name']} ({s['marks']})")
    else:
        print("No records found.")


def sort_records():
    data = load_data()
    choice = input("Sort by (1) Name (2) Marks: ")
    if choice == '1':
        data.sort(key=lambda x: x['name'])
    elif choice == '2':
        data.sort(key=lambda x: x['marks'], reverse=True)
    for s in data: print(f"{s['roll_no']} - {s['name']} ({s['marks']})")


def generate_reports():
    data = load_data()
    if not data:
        print("No data.")
        return
    avg = sum(s['marks'] for s in data) / len(data)
    topper = max(data, key=lambda x: x['marks'])
    print(f"Average Marks: {avg:.2f}")
    print(f"Topper: {topper['name']} ({topper['marks']})")


def main():
    if not authenticate():
        return

    while True:
        print("\n1. Add 2. Search 3. Sort 4. Report 5. Exit")
        ch = input("Choice: ")
        if ch == '1':
            add_student()
        elif ch == '2':
            search_student()
        elif ch == '3':
            sort_records()
        elif ch == '4':
            generate_reports()
        elif ch == '5':
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()