def operations(storage_dict):
    # storage = {plant: {'RARITY': rarity,'RATING' []}}
    while True:
        command = input().split(": ")
        if command[0] == "Exhibition":
            break
        current_command = command[0]
        command_elements = command[1].split(" - ")
        if current_command == "Rate":
            current_plant = command_elements[0]
            current_rating = float(command_elements[1])
            if current_plant not in storage_dict:
                print("error")
            else:
                storage_dict[current_plant]['RATING'].append(current_rating)
        elif current_command == "Update":
            current_plant = command_elements[0]
            new_rarity = command_elements[1]
            if current_plant not in storage_dict:
                print("error")
            else:
                storage_dict[current_plant]['RARITY'] = new_rarity
        elif current_command == "Reset":
            current_plant = command_elements[0]
            if current_plant not in storage_dict:
                print("error")
            else:
                storage_dict[current_plant]['RATING'] = []

    return storage_dict


number_of_times = int(input())
storage = {}
# storage = {plant: {'RARITY': rarity,'RATING' []}}
for _ in range(number_of_times):
    plant, rarity = input().split("<->")
    if plant not in storage:
        storage[plant] = {'RARITY': rarity, 'RATING': []}
    else:
        storage[plant]['RARITY'] = rarity
        storage[plant]['RATING'] = []
storage = operations(storage)

for name, elements in storage.items():
    if not storage[name]['RATING']:
        storage[name]['RATING'] = 0
    else:
        storage[name]['RATING'] = sum(storage[name]['RATING']) / len(storage[name]['RATING'])
print('Plants for the exhibition:')
for current_plant, value in storage.items():
    print(f"- {current_plant}; Rarity: {value['RARITY']}; Rating: {value['RATING']:.2f}")