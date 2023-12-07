some_text = input()
for index, symbol in enumerate(some_text):
    if symbol == ":" and index < len(some_text) - 1:
        print(f"{some_text[index]}{some_text[index+1]}")