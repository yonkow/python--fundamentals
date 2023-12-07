import re

pattern = r'((^|(?<=\s))([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z]+[a-z\-]*(\.[a-z]+)+)\b)'
sentence = input()
matches = re.findall(pattern, sentence)
for match in matches:
    print(match[0])