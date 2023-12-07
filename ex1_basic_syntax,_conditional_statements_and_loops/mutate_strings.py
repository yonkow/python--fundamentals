first_word = input()
second_word = input()
last_printed_word = ""
for i in range(len(first_word)):
    left_part = second_word[: i+1]
    right_part = first_word[i+1:]
    current_word = left_part + right_part
    if last_printed_word == current_word:
        continue
    else:
        last_printed_word = current_word
        print(current_word)