string = input()
while True:
    command = input().split()
    if command[0] == 'Done':
        break
    current_command = command[0]
    if current_command == 'Change':
        char, replacement = command[1:]
        string = string.replace(char, replacement)
        print(string)
    elif current_command == 'Includes':
        substring = command[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif current_command == 'End':
        substring = command[1]
        index = -len(substring)
        if substring == string[index:]:
            print("True")
        else:
            print("False")
    elif current_command == 'Uppercase':
        string = string.upper()
        print(string)
    elif current_command == 'FindIndex':
        char = command[1]
        index = string.find(char)
        print(index)
    elif current_command == 'Cut':
        start_index, count = int(command[1]), int(command[2])
        string = string[start_index:start_index+count]
        print(string)