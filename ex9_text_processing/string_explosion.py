some_text = input()
strength = 0
final_string = ""
for index in range(len(some_text)):
    if some_text[index] == ">":
        strength += int(some_text[index+1])
        final_string += some_text[index]
    elif some_text[index] != ">" and strength == 0:
        final_string += some_text[index]
    else:
        strength -= 1
print(final_string)