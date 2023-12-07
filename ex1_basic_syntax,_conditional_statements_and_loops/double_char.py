current_string = input()
while current_string != "End":
    if current_string != "SoftUni":
        for letter in current_string:
            print(f"{letter}{letter}", end="")
        print()
    current_string = input()