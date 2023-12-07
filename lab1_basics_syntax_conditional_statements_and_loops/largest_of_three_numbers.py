import sys

max_num = -sys.maxsize
for current_number in range(0, 3):
    num = int(input())
    if num > max_num:
        max_num = num
print(max_num)