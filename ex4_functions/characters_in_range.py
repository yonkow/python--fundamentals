def char_in_range(first: int, second: int):
    character_lst = []
    for index in range(first+1, second):
        character = chr(index)
        character_lst.append(character)
    return character_lst


first_char = ord(input())
second_char = ord(input())
print(" ".join(char_in_range(first_char, second_char)))