some_string = input()
last_letter = ""
for letter in some_string:
    if letter != last_letter:
        last_letter = letter
        print(letter, end="")