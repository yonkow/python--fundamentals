activation_key = input()
while True:
    command = input().split(">>>")
    if command[0] == "Generate":
        print(f"Your activation key is: {activation_key}")
        break
    current_command = command[0]
    if current_command == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif current_command == "Flip":
        upper_lower, start_index, end_index = command[1], int(command[2]), int(command[3])
        if upper_lower == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() \
                             + activation_key[end_index:]
        elif upper_lower == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() \
                             + activation_key[end_index:]
        print(activation_key)
    elif current_command == "Slice":
        start_index, end_index = int(command[1]), int(command[2])
        activation_key = activation_key.replace(activation_key[start_index:end_index], "")
        print(activation_key)