lst_of_numbers = input().split()
numbers_of_iterations = int(input())
for i in range(len(lst_of_numbers)):
    lst_of_numbers[i] = int(lst_of_numbers[i])

for _ in range(numbers_of_iterations):
    lst_of_numbers.remove(min(lst_of_numbers))

print(*lst_of_numbers, sep=", ")