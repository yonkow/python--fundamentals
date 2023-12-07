some_text = input()
new_text = ""
for char in some_text:
    new_text += chr(ord(char) + 3)
print(new_text)