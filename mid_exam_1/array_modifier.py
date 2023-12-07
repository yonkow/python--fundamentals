def swap(array: list, first: int, second: int):
    array[first], array[second] = array[second], array[first]
    return array


def multiply(array: list, first: int, second: int):
    out = array[first] * array[second]
    array[first] = out
    return array


def decrease(array: list):
    array = [value - 1 for value in array]
    return array


array_lst = [int(num) for num in input().split()]
flag = False
while True:
    current_command = input().split()
    command = current_command[0]
    if command == "end":
        flag = True
        break
    if command == "swap":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        array_lst = swap(array_lst, first_index, second_index)
    elif command == "multiply":
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        array_lst = multiply(array_lst, first_index, second_index)
    elif command == "decrease":
        array_lst = decrease(array_lst)

print(', '.join(str(i) for i in array_lst))