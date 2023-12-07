import re

pattern = r'(\!)([A-Z][a-z]{2,})\1\:{1}\[([A-Za-z]{8,})\]'
number_of_string = int(input())
for _ in range(number_of_string):
    current_string = input()
    matches = re.findall(pattern, current_string)
    if len(matches) > 0:
        for match in matches:
            command = match[1]
            message = match[2]
            translated_message = ''
            for letter in message:
                translated_message += f' {ord(letter)}'
            print(f"{command}:{translated_message}")
    else:
        print("The message is invalid")