number_of_letters = int(input())
total_sum = 0
for letters in range(number_of_letters):
    current_letter = input()
    total_sum += ord(current_letter)
print(f"The sum equals: {total_sum}")