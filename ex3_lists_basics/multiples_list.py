factor = int(input())
count = int(input())
multiple_lst = []

for current_counter in range(1, count + 1):
    current_number = current_counter * factor
    multiple_lst.append(current_number)

print(multiple_lst)