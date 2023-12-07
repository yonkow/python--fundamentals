import re

pattern = r"www\.[A-Za-z0-9\-]+(\.[a-z]+){1,}"
text = input()

while text:
    matches = re.search(pattern, text)
    if matches:
        print(matches.group())
    text = input()


