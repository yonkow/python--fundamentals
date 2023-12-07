courses = {}
while True:
    command = input().split(' : ')
    if len(command) == 1:
        break
    course_name, student_name = command[0], command[1]
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name] += [student_name]
for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")