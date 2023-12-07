def even_numbers(number):
    if number % 2 != 0:
        return False
    return True


list_of_numbers = input().split()
list_of_numbers = list(map(int, list_of_numbers))
even_numbers_iterator = filter(even_numbers, list_of_numbers)
even_lst = list(even_numbers_iterator)
print(even_lst)