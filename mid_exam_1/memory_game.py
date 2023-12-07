def memory_game(elements: list, index: list, number_of_moves):
    first_index, second_index = index[0], index[1]
    if first_index == second_index or first_index < 0 or second_index < 0 \
            or first_index >= len(elements) or second_index >= len(elements):
        i = len(elements) // 2
        additional_element = f"-{number_of_moves}a"
        elements.insert(i, additional_element)
        elements.insert(i + 1, additional_element)
        print("Invalid input! Adding additional elements to the board")
    elif elements[first_index] == elements[second_index]:
        if first_index > second_index:
            removed_element = elements.pop(second_index)
            elements.pop(first_index - 1)
            print(f"Congrats! You have found matching elements - {removed_element}!")
        elif first_index < second_index:
            removed_element = elements.pop(first_index)
            elements.pop(second_index - 1)
            print(f"Congrats! You have found matching elements - {removed_element}!")
    elif elements[first_index] != elements[second_index]:
        print("Try again!")

    return elements


lst_of_elements = input().split()
command = input()
moves = 0
lose_condition = False
while True:
    current_indexes = [int(i) for i in command.split()]
    moves += 1
    lst_of_elements = memory_game(lst_of_elements, current_indexes, moves)
    if len(lst_of_elements) == 0:
        print(f"You have won in {moves} turns!")
        break
    command = input()
    if command == "end":
        lose_condition = True
        break
if lose_condition:
    print(f"""Sorry you lose :(
{' '.join(lst_of_elements)}""")