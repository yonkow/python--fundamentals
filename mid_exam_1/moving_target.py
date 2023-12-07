def moving_target(target: list, move: str, index: int, value: int):
    if move == "Shoot" and 0 <= index < len(target):
        target[index] -= value
        if target[index] <= 0:
            target.pop(index)

    elif move == "Add":
        if 0 <= index < len(target):
            target.insert(index, value)
        else:
            print("Invalid placement!")

    elif move == "Strike":
        left_range = index - value
        right_range = index + value
        removed_items = []
        if left_range >= 0 and right_range < len(target):
            for current_i in range(len(target)):
                if current_i in range(left_range, right_range + 1):
                    removed_items.append(target[current_i])
            for item in removed_items:
                target.remove(item)
        else:
            print("Strike missed!")

    return target


lst_targets = [int(index) for index in input().split()]
command = input()
while command != "End":
    current_command, index_as_str, value_as_str = command.split()
    current_index = int(index_as_str)
    current_value = int(value_as_str)
    lst_targets = moving_target(lst_targets, current_command, current_index, current_value)
    command = input()

print("|".join(str(item) for item in lst_targets))