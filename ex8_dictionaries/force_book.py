force_book = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        splitted_command = command.split(" | ")
        force_side, force_user = splitted_command
        is_in_side = False
        for value in force_book.values():
            if force_user in value:
                is_in_side = True
                break
        if not is_in_side and force_side not in force_book.keys():
            force_book[force_side] = [force_user]
        elif not is_in_side:
            force_book[force_side].append(force_user)
    elif "->" in command:
        splitted_command = command.split(" -> ")
        force_user, force_side = splitted_command
        for key, value in force_book.items():
            if force_user in value:
                force_book[key].pop(value.index(force_user))
                break

        if force_side not in force_book.keys():
            force_book[force_side] = [force_user]
        else:
            force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for force_side, force_users in force_book.items():
    if len(force_users) > 0:
        print(f"Side: {force_side}, Members: {len(force_users)}")
        for user in force_users:
            print(f"! {user}")