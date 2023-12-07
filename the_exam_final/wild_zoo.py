def feeding(animals, com):
    animal_name, food = com.split('-')
    food = int(food)
    if animal_name in animals:
        animals[animal_name]['F'] -= food
        if animals[animal_name]['F'] <= 0:
            print(f"{animal_name} was successfully fed")
            del animals[animal_name]
    return animals


def add_hungry_animals(animals, com):
    animal_name, food_quantity, area = com.split('-')
    food_quantity = int(food_quantity)
    if animal_name not in animals:
        animals[animal_name] = {'F': food_quantity, 'A': area}
    else:
        animals[animal_name]['F'] += food_quantity
    return animals


hungry_animals = {}
areas = {}
# {animal: {'F': food, 'A': area}}
while True:
    command = input().split(': ')
    if command[0] == 'EndDay':
        break
    current_command = command[0]
    if current_command == 'Add':
        hungry_animals = add_hungry_animals(hungry_animals, command[1])
    elif current_command == 'Feed':
        hungry_animals = feeding(hungry_animals, command[1])
print("Animals:")
for name, value in hungry_animals.items():
    print(f" {name} -> {value['F']}g")
    if value['A'] not in areas:
        areas[value['A']] = []
        areas[value['A']].append(name)
    else:
        areas[value['A']].append(name)
print("Areas with hungry animals:")
for current_area, current_animals in areas.items():
    print(f" {current_area}: {len(current_animals)}")