import re

some_text = input()
pattern = r"(=|\/)([A-Z]{1}[a-zA-Z]{2,})\1"

matches = re.findall(pattern, some_text)
destinations = []
sum_lens = 0
for match in matches:
    destinations.append(match[1])
    sum_lens += len(match[1])
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {sum_lens}")
