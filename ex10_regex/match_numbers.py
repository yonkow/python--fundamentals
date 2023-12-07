import re

inserted_text = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(pattern, inserted_text)
for number in matches:
    print(number.group(), end=" ")
