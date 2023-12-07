parking_lot = {}

number_of_commands = int(input())
for i in range(number_of_commands):
    command = input().split()
    current_command, current_username = command[0], command[1]
    if current_command == "register":
        plate_number = command[2]
        if current_username not in parking_lot:
            parking_lot[current_username] = plate_number
            print(f"{current_username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif current_command == "unregister":
        if current_username not in  parking_lot:
            print(f"ERROR: user {current_username} not found")
        else:
            print(f"{current_username} unregistered successfully")
            del parking_lot[current_username]

for current_username, plate_number in parking_lot.items():
    print(f"{current_username} => {plate_number}")