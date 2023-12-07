sequence = input()
while True:
    command = input().split(":")
    if command[0] == "Travel":
        print(f"Ready for world tour! Planned stops: {sequence}")
        break
    current_command = command[0]
    if current_command == "Add Stop":
        index = int(command[1])
        string = command[2]
        if 0 <= index < len(sequence):
            sequence = sequence[:index] + string + sequence[index:]
    elif current_command == "Remove Stop":
        start_index, end_index = int(command[1]), int(command[2])
        if 0 <= start_index <= end_index < len(sequence):
            sequence = sequence[:start_index] + sequence[end_index+1:]
    elif current_command == "Switch":
        old_string, new_string = command[1:]
        sequence = sequence.replace(old_string, new_string, 1)
    print(sequence)