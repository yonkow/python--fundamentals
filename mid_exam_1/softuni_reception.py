first_employer = int(input())
second_employer = int(input())
third_employer = int(input())
employee_efficiency_per_hour = first_employer + second_employer + third_employer
student_count = int(input())
hour_counter = 0
while True:
    if student_count <= 0:
        break
    hour_counter += 1
    if hour_counter % 4 != 0:
        student_count -= employee_efficiency_per_hour
    else:
        continue
print(f"Time needed: {hour_counter}h.")