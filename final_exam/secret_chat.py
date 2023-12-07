def crypter(message: str):
    while True:
        command = input().split(":|:")
        if command[0] == "Reveal":
            break
        current_command = command[0]
        if current_command == "InsertSpace":
            index = int(command[1])
            if index <= (len(message)):
                message = message[:index] + " " + message[index:]
        elif current_command == "Reverse":
            substring = command[1]
            if substring in message:
                message = message.replace(substring, "", 1)
                message = message + substring[::-1]
            else:
                print("error")
                continue
        elif current_command == "ChangeAll":
            substring, replacement = command[1], command[2]
            message = message.replace(substring, replacement)
        print(message)

    return message


text_message = input()
decrypted_text = crypter(text_message)
print(f"You have a new text message: {decrypted_text}")