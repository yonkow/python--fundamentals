import sys

divisor = int(input())
boundary = int(input())
max_number = -sys.maxsize
for current_number in range(1, boundary + 1):
    if current_number % divisor == 0 and max_number <= current_number:
        max_number = current_number
    else:
        continue
print(max_number)