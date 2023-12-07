def operations(cars, command):
    current_command = command[0]
    if current_command == "Drive":
        car, distance, fuel = command[1], int(command[2]), int(command[3])
        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            del cars[car]
    elif current_command == "Refuel":
        car, fuel = command[1], int(command[2])
        if cars[car][1] + fuel > 75:
            fuel = 75 - cars[car][1]
            cars[car][1] += fuel
        else:
            cars[car][1] += fuel
        print(f"{car} refueled with {fuel} liters")
    elif current_command == "Revert":
        car, kilometers = command[1], int(command[2])
        cars[car][0] -= kilometers
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars


def pieces_collection(n):
    # collection type: {car: [mileage, fuel]}
    cars = {}
    for _ in range(n):
        current_cars = input().split("|")
        car, mileage, fuel = current_cars[0], int(current_cars[1]), int(current_cars[2])
        cars[car] = [mileage, fuel]
    while True:
        command = input().split(" : ")
        if command[0] == "Stop":
            break
        else:
            cars = operations(cars, command)
    return cars


number_of_cars = int(input())
collections = pieces_collection(number_of_cars)

for current_car, values in collections.items():
    current_mileage, current_fuel = values
    print(f"{current_car} -> Mileage: {current_mileage} kms, Fuel in the tank: {current_fuel} lt.")