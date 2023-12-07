def forward_command(lst_command, houses, current_position):
    steps = int(lst_command[1])
    if 0 <= current_position + steps < len(houses):
        current_position += steps
        houses.pop(current_position)

    return current_position, houses


def back_command(lst_command, houses, current_position):
    steps = int(lst_command[1])
    if 0 <= current_position - steps < len(houses):
        current_position -= steps
        houses.pop(current_position)

    return current_position, houses


def gift_command(lst_command: list, houses: list, current_position):
    index = int(lst_command[1])
    new_house = int(lst_command[2])
    if 0 <= index < len(houses):
        current_position = index
        houses.insert(index, new_house)

    return current_position, houses


def swap_command(lst_command, houses):
    first_number = int(lst_command[1])
    second_number = int(lst_command[2])
    if first_number in houses and second_number in houses:
        first_index = houses.index(first_number)
        second_index = houses.index(second_number)
        if 0 <= first_index < len(houses) and 0 <= second_index < len(houses):
            houses[first_index], houses[second_index] = houses[second_index], houses[first_index]

    return houses


def santa_gift(iteration: int, houses: list):
    current_position = 0
    for _ in range(iteration):
        lst_command = [something for something in input().split()]
        command = lst_command[0]
        if command == "Forward":
            current_position, houses = forward_command(lst_command, houses, current_position)
        elif command == "Back":
            current_position, houses = back_command(lst_command, houses, current_position)
        elif command == "Gift":
            current_position, houses = gift_command(lst_command, houses, current_position)
        elif command == "Swap":
            houses = swap_command(lst_command, houses)
    return current_position, houses


num_of_given_commands = int(input())
lst_of_num_houses = [int(number) for number in input().split() if 0 < int(number) <= 1000]

position, lst_of_num_houses = santa_gift(num_of_given_commands, lst_of_num_houses)
lst_of_houses_as_string = [str(number) for number in lst_of_num_houses]

print(f"""Position: {position}
{', '.join(lst_of_houses_as_string)}""")