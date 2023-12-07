import re

some_text = input()
pattern = r"(@|#)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"
mirror_words = []
matched_words = re.findall(pattern, some_text)
if not matched_words:
    print("No word pairs found!")
else:
    print(f"{len(matched_words)} word pairs found!")
for match in matched_words:
    word_one, word_two = match[1], match[2]
    if word_one == word_two[::-1]:
        mirror_words.append(f"{word_one} <=> {word_two}")

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))