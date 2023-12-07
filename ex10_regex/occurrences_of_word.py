import re

some_text = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, some_text, flags=re.IGNORECASE)
print(len(matches))