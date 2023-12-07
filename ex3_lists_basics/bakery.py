def command_rest(current_energy, current_number):
    total_energy = current_energy
    current_energy += current_number
    if current_energy > 100:
        current_energy = 100
    gained_energy = current_energy - total_energy
    print(f"You gained {gained_energy} energy.")
    print(f"Current energy: {current_energy}.")
    return current_energy


def command_order(current_coins, current_energy, current_number):
    if current_energy >= 30:
        current_energy -= 30
        print(f"You earned {current_number} coins.")
        current_coins += current_number
    else:
        print("You had to rest!")
        current_energy += 50
    return current_coins, current_energy


def command_ingredient(current_coins, current_number, current_ingredient, bakery):
    if current_coins >= current_number:
        print(f"You bought {current_ingredient}.")
        current_coins -= current_number
    else:
        bakery = True
    return current_coins, bakery


coins = 100
energy = 100
lst_event_and_number = input().split("|")
closed_bakery = False
for event_number in lst_event_and_number:
    if closed_bakery:
        break
    event, number = event_number.split("-")
    if event == "rest":
        energy = command_rest(energy, int(number))
    elif event == "order":
        coins, energy = command_order(coins, energy, int(number))
    else:
        coins, closed_bakery = command_ingredient(coins, int(number), event, closed_bakery)

if closed_bakery:
    print(f"Closed! Cannot afford {event}.")
else:
    print(f"""Day completed! 
Coins: {coins}
Energy: {energy}""")