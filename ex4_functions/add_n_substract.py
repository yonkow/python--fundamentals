def sum_numbers(first: int, second: int):
    return first + second


def subtract(first_two: int, third: int):
    return first_two - third


def add_and_subtract(first, second, third):
    sum_of_first_two = sum_numbers(first, second)
    difference = subtract(sum_of_first_two, third)
    return difference


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(add_and_subtract(first_num, second_num, third_num))