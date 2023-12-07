import re


def alphabet_digit_separator(string, letter, digit):
    letters = re.findall(letter, string)
    name = ''.join(letters)
    distance = 0
    digits = re.findall(digit, string)
    if digits:
        for digit in digits:
            distance += int(digit)
    return name, distance


def one_race(participants_, name, distance, races):

    if name in participants_:
        if name not in races:
            races[name] = distance
        else:
            races[name] += distance
    return races


def the_race(participants_):
    final_races = {}
    while True:
        command = input()
        if command == "end of race":
            break

        racer, length = alphabet_digit_separator(command, letter_pattern, digit_pattern)
        final_races = one_race(participants_, racer, length, final_races)

    return final_races


letter_pattern = r"[A-Za-z]+"
digit_pattern = r"\d"

participants = input().split(", ")
table_of_races = the_race(participants)

table_of_races = {k: v for k, v in sorted(table_of_races.items(), key=lambda item: item[1])}
print(table_of_races)