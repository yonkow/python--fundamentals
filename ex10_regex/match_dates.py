import re

inserted_text = input()
pattern = r"\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b"
matches = re.findall(pattern, inserted_text)
for day, sep, month, year in matches:
    print(f"Day: {day}, Month: {month}, Year: {year}")