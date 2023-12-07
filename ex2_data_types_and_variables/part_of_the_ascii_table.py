starting_char = int(input())
finishing_char = int(input())
for letter_positions in range(starting_char, finishing_char + 1):
    print(chr(letter_positions), end=" ")