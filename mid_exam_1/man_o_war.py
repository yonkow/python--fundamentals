def fire(warriors, index, damage):
    sunken_warriors = False
    if 0 <= index < len(warriors):
        warriors[index] -= damage
        if warriors[index] == 0:
            sunken_warriors = True
            print("You won! The enemy ship has sunken.")
    return warriors, sunken_warriors


def defend(pirates, start, end, damage):
    sunken_pirates = False
    if 0 <= start < end < len(pirates):
        for i in range(start, end + 1):
            pirates[i] -= damage
        for section in pirates:
            if section <= 0:
                sunken_pirates = True
                print("You lost! The pirate ship has sunken.")
                break
    return pirates, sunken_pirates


def repair(pirates, index, heal, maximum):
    if 0 <= index < len(pirates):
        pirates[index] += heal
        if pirates[index] > maximum:
            pirates[index] = maximum
    return pirates


def status(pirates, maximum):
    counter_pirates_status = [state for state in pirates if (state / maximum) * 100 < 20]
    return counter_pirates_status


pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
maximum_health = int(input())
flag = False

while True:
    command = input().split()
    current_command = command[0]
    if current_command == "Retire":
        flag = True
        break
    if current_command == "Fire":
        current_index = int(command[1])
        current_damage = int(command[2])
        war_ship, sunken_warship = fire(war_ship, current_index, current_damage)
        if sunken_warship:
            break
    elif current_command == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        current_damage = int(command[3])
        pirate_ship, sunken_pirate_ship = defend(pirate_ship, start_index, end_index, current_damage)
        if sunken_pirate_ship:
            break
    elif current_command == "Repair":
        current_index = int(command[1])
        current_heal = int(command[2])
        pirate_ship = repair(pirate_ship, current_index, current_heal, maximum_health)
    elif current_command == "Status":
        counter = status(pirate_ship, maximum_health)
        print(f"{len(counter)} sections need repair.")

if flag:
    print(f"""Pirate ship status: {sum(pirate_ship)}
Warship status: {sum(war_ship)}""")