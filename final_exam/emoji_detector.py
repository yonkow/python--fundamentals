import re


def threshold(text):
    cool_number = 1
    pattern = r"\d"
    matches = re.findall(pattern, text)
    for match in matches:
        cool_number *= int(match)
    return cool_number


def emoji_finder(text):
    pattern = r"(:|\*){2}([A-Z]{1}[a-z]{2,})\1{2}"
    emojis = re.findall(pattern, text)
    return emojis


def ascii_emoji(current):
    sum_emoji = 0
    for letter in current:
        sum_emoji += ord(letter)
    return sum_emoji


def print_function(emoji_lst, cool_threshold_sum):
    print_one = f"Cool threshold: {cool_threshold_sum}"
    print_two = f"{len(emoji_lst)} emojis found in the text. The cool ones are:"
    print_three = ""
    for current in emoji_lst:
        char = current[0]
        current_emoji = current[1]
        if ascii_emoji(current_emoji) >= cool_threshold_sum:
            print_three += f"{char}{char}{current_emoji}{char}{char}\n"
    return print_one, print_two, print_three


some_text = input()
cool_threshold = threshold(some_text)
emoji_list = emoji_finder(some_text)
first_print, second_print, third_print = print_function(emoji_list, cool_threshold)
print(first_print)
print(second_print)
print(third_print)
