numbers_of_rows = int(input())
class_book = {}
for i in range(numbers_of_rows):
    current_student = input()
    current_grade = float(input())
    if current_student not in class_book:
        class_book[current_student] = []
    class_book[current_student] += [current_grade]

for student, grades in class_book.items():
    average = sum(grades) / len(grades)
    if average >= 4.5:
        print(f"{student} -> {average:.2f}")