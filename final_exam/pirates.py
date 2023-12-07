def attack(cities):
    while True:
        command = input().split("=>")
        if command[0] == "End":
            break
        current_command = command[0]
        if current_command == "Plunder":
            town, people, gold = command[1], int(command[2]), int(command[3])
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            cities[town]['PEOPLE'] -= people
            cities[town]['GOLD'] -= gold
            if cities[town]['PEOPLE'] <= 0 or cities[town]['GOLD'] <= 0:
                print(f"{town} has been wiped off the map!")
                del cities[town]
        elif current_command == "Prosper":
            town, gold = command[1], int(command[2])
            if gold >= 0:
                cities[town]['GOLD'] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['GOLD']} gold.")
            else:
                print("Gold added cannot be a negative number!")
    return cities


def targeting_cities(cities):
    while True:
        command = input().split("||")
        if command[0] == "Sail":
            break
        current_city, population, gold = command[0], int(command[1]), int(command[2])
        if current_city not in cities:
            cities[current_city] = {'PEOPLE': population, 'GOLD': gold}
        else:
            cities[current_city]['PEOPLE'] += population
            cities[current_city]['GOLD'] += gold
    cities = attack(cities)
    return cities


targeted_cities = {} # targeted_cities = {current_city: [population, gold]}
targeted_cities = targeting_cities(targeted_cities)
if len(targeted_cities) > 0:
    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for current_town, elements in targeted_cities.items():
        current_people, amount_of_gold = elements['PEOPLE'], elements['GOLD']
        print(f"{current_town} -> Population: {current_people} citizens, Gold: {amount_of_gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")