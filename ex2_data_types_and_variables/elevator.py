import math

number_of_persons = int(input())
capacity = int(input())
courses = number_of_persons / capacity
if courses != 0:
    print(math.ceil(courses))
else:
    print(math.ceil(courses))