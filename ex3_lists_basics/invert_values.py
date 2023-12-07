lst_of_numbers = input().split()
opposite_lst_of_numbers = []

for elements in lst_of_numbers:
    concurrent_number = -int(elements)
    opposite_lst_of_numbers.append(concurrent_number)

print(opposite_lst_of_numbers)