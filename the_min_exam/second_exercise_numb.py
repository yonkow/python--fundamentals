def add(numbs, value):
    numbs.append(value)
    return numbs


def remove(numbs, value):
    if value in numbs:
        numbs.remove(value)
    return numbs


def replacement(numbs, value, replace):
    if value in numbs:
        index = numbs.index(value)
        numbs[index] = replace
    return numbs


def collapse(numbs, value):
    lst_copy = numbs.copy()
    for num in lst_copy:
        if num < value:
            numbs.remove(num)
    return numbs


lst_of_numbs = list(map(int, input().split()))
while True:
    command = input().split()
    if command[0] == "Finish":
        break
    current_command = command[0]
    current_value = int(command[1])
    if current_command == "Add":
        lst_of_numbs = add(lst_of_numbs, current_value)
    elif current_command == "Remove":
        lst_of_numbs = remove(lst_of_numbs, current_value)
    elif current_command == "Replace":
        current_replacement = int(command[2])
        lst_of_numbs = replacement(lst_of_numbs, current_value, current_replacement)
    elif current_command == "Collapse":
        lst_of_numbs = collapse(lst_of_numbs, current_value)

print(' '.join(str(numb) for numb in lst_of_numbs))