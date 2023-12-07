def reset_pass(raw_password):
    final_password = ''
    while True:
        command = input().split(' ')
        if command[0] == 'Done':
            break
        current_command = command[0]
        if current_command == 'TakeOdd':
            for letter in raw_password[1::2]:
                final_password += letter
            print(final_password)
            raw_password = final_password
        elif current_command == 'Cut':
            index, length = int(command[1]), int(command[2])
            if index + length <= len(raw_password):
                substring = raw_password[index:index+length]
                raw_password = raw_password.replace(substring, '', 1)
            print(raw_password)
        elif current_command == 'Substitute':
            substring, substitute = command[1:]
            if substring in raw_password:
                raw_password = raw_password.replace(substring, substitute)
                print(raw_password)
            else:
                print("Nothing to replace!")
    return raw_password


password = input()
new_password = reset_pass(password)
print(f"Your password is: {new_password}")