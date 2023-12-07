phonebook = {}
while True:
    command = input().split('-')
    if len(command) == 1:
        break
    name, number = command[0], command[1]
    if name in phonebook:
        phonebook[name] = number
    phonebook[name] = number
iterations = int(command[0])
for _ in range(iterations):
    searched_name = input()
    if searched_name in phonebook.keys():
        number = phonebook[searched_name]
        print(f"{searched_name} -> {number}")
    else:
        print(f"Contact {searched_name} does not exist.")