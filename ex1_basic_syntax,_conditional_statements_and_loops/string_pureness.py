number_of_times = int(input())
for current_check in range(number_of_times):
    current_string = input()
    is_pure = True
    for index in current_string:
        if index == "," or index == "." or index == "_":
            is_pure = False
        else:
            continue
    if is_pure:
        print(f"{current_string} is pure.")
    else:
        print(f"{current_string} is not pure!")