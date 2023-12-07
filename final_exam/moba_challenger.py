tier = {}
# tier = {'player': ['position', skill]}
while True:
    command = input()
    if command == "Season end":
        break
    if ' -> ' in command:
        current_command = command.split(' -> ')
        player, position, skill = current_command[0], current_command[1], int(current_command[2])
        if player not in tier:
            tier[player] = {}
            tier[player][position] = skill
        else:
            if position not in tier[player]:
                tier[player][position] = skill
            else:
                if tier[player][position] < skill:
                    tier[player][position] = skill
    if ' vs ' in command:
        current_command = command.split(' vs ')
        player_one, player_two = current_command[0], current_command[1]
        if player_one in tier and player_two in tier:
            print(tier[player_one][value])

for name, values in tier.items():
    total_skill = 0
    roles = ''
    for position, skill in values.items():
        total_skill += skill
        roles += f'- {position} <::> {skill}\n'
    print(f"{name}: {total_skill} skill")
    print(roles, end='')