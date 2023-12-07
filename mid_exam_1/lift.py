def place_finder(people: int, free_spaces: list):
    for index, wagon in enumerate(free_spaces):
        fill_spaces = wagon
        if fill_spaces <= 4 and people > 0:
            current_free_spaces = 4 - fill_spaces
            if people >= current_free_spaces:
                free_spaces[index] += current_free_spaces
            elif people < current_free_spaces:
                free_spaces[index] += people
            people -= current_free_spaces
    if people < 0:
        people = 0
    return people, free_spaces


waiting_people = int(input())
lift_composition = [int(number) for number in input().split()]
waiting_people, lift_composition = place_finder(waiting_people, lift_composition)
empty_spots = (len(lift_composition) * 4) - sum(lift_composition)

if waiting_people == 0 and empty_spots > 0:
    print(f"""The lift has empty spots!
{' '.join(str(wagons) for wagons in lift_composition)}""")

elif waiting_people > 0 and empty_spots <= 0:
    print(f"""There isn't enough space! {waiting_people} people in a queue!
{' '.join(str(wagons) for wagons in lift_composition)}""")

elif waiting_people == 0 and empty_spots == 0:
    print(f"{' '.join(str(wagons) for wagons in lift_composition)}")