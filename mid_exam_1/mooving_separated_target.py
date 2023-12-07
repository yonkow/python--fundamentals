def shoot_condition(target, index, value):
    target[index] -= value
    if target[index] <= 0:
        target.pop(index)
    return target


def add_condition(target, index, value, exist):
    if exist:
        target.insert(index, value)
    else:
        print("Invalid placement!")
    return target


def strike_condition(target, index, value):
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
    index_exist = False

    if 0 <= current_index < len(lst_targets):
        index_exist = True

    if current_command == "Shoot" and index_exist:
        lst_targets = shoot_condition(lst_targets, current_index, current_value)
    elif current_command == "Add":
        lst_targets = add_condition(lst_targets, current_index, current_value, index_exist)
    elif current_command == "Strike":
        lst_targets = strike_condition(lst_targets, current_index, current_value)
    command = input()

print("|".join(str(item) for item in lst_targets))