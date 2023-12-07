def smallest_number(numbers: list):
    return min(numbers)


first_num = int(input())
second_num = int(input())
third_num = int(input())
lst_of_numbers = [first_num, second_num, third_num]
min_number = smallest_number(lst_of_numbers)
print(min_number)