current_string = input().split()
current_simbols = ''.join(current_string)
string_counter = {}
for char in current_simbols:
    if char not in string_counter:
        string_counter[char] = 0
    string_counter[char] += 1
for char, occurrences in string_counter.items():
    print(f"{char} -> {occurrences}")