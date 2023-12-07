name_of_the_gifts = input().split()
current_command = input()

while current_command != "No Money":
    command_list = current_command.split()
    if command_list[0] == "OutOfStock":
        for gift in range(len(name_of_the_gifts)):
            if name_of_the_gifts[gift] == command_list[-1]:
                name_of_the_gifts[gift] = "None"
    elif command_list[0] == "Required":
        index_of_gift = int(command_list[-1])
        if index_of_gift >= 0 and len(name_of_the_gifts) > index_of_gift:
            name_of_the_gifts[index_of_gift] = command_list[1]
    elif command_list[0] == "JustInCase":
        name_of_the_gifts[-1] = command_list[-1]
    current_command = input()

last_list = list(filter(lambda word: word != "None", name_of_the_gifts))
print(" ".join(last_list))