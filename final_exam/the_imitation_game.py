string_message = input()
while True:
    command = input().split("|")
    if command[0] == "Decode":
        break
    current_command = command[0]
    if current_command == "Move":
        number_of_letters = int(command[1])
        string_message = string_message[number_of_letters:] + string_message[:number_of_letters]
    elif current_command == "Insert":
        index, value = int(command[1]), command[2]
        string_message = string_message[:index] + value + string_message[index:]
    elif current_command == "ChangeAll":
        substring, replacement = command[1], command[2]
        string_message = string_message.replace(substring, replacement)
print(f"The decrypted message is: {string_message}")