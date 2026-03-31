def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a number.")

def get_non_empty_string(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Cannot be empty.")