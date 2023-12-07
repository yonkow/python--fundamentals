def cupids_work(lst_hearts: list, done):
    current_position = 0
    while True:
        command = input().split()
        current_command = command[0]
        if current_command == "Love!":
            break
        current_length = int(command[1])
        current_position += current_length
        if 0 <= current_position < len(lst_hearts):
            if lst_hearts[current_position] == 0:
                print(f"Place {current_position} already had Valentine's day.")
            else:
                lst_hearts[current_position] -= 2
                if lst_hearts[current_position] == 0:
                    print(f"Place {current_position} has Valentine's day.")
        elif 0 > current_position or current_position >= len(lst_hearts):
            current_position = 0
            if lst_hearts[current_position] == 0:
                print(f"Place {current_position} already had Valentine's day.")
            else:
                lst_hearts[current_position] -= 2
                if lst_hearts[current_position] == 0:
                    print(f"Place {current_position} has Valentine's day.")
        if sum(lst_hearts) == 0:
            done = True
            break
    return done, current_position, lst_hearts


flag = False
number_of_hearts_in_houses = [int(number) for number in input().split("@") if int(number) % 2 == 0]
flag, position, number_of_hearts_in_houses = cupids_work(number_of_hearts_in_houses, flag)
number_of_hearts_in_houses = [num for num in number_of_hearts_in_houses if num != 0]
counter = len(number_of_hearts_in_houses)
print(f"Cupid's last position was {position}.")
if flag:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")