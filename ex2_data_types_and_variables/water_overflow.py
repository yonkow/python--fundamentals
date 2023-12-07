tank_capacity = 255
poured_volume = 0
number_of_pour = int(input())
for _ in range(number_of_pour):
    current_liters = int(input())
    if tank_capacity >= poured_volume + current_liters:
        poured_volume += current_liters
    else:
        print("Insufficient capacity!")
print(poured_volume)