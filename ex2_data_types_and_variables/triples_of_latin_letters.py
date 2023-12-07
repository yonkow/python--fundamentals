counter = int(input())
ascii_char = 97
for letter1 in range(counter):
    for letter2 in range(counter):
        for letter3 in range(counter):
            print(f"{chr(ascii_char + letter1)}{chr(ascii_char + letter2)}{chr(ascii_char + letter3)}")
print()