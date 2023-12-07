def duel(tier_dict, first_player, second_player):
    if len(tier_dict[first_player]['P']) > len(tier_dict[second_player]['P']):
        for current_position in tier_dict[first_player]['P']:
            if current_position in tier_dict[second_player]['P']:
                total_sum_first = sum(tier_dict[first_player]['S'])
                total_sum_second = sum(tier_dict[second_player]['S'])
                if total_sum_first < total_sum_second:
                    del tier_dict[first_player]
                elif total_sum_first > total_sum_second:
                    del tier_dict[second_player]
    elif len(tier_dict[first_player]['P']) < len(tier_dict[second_player]['P']):
        for current_position in tier_dict[second_player]['P']:
            if current_position in tier_dict[first_player]['P']:
                total_sum_first = sum(tier_dict[first_player]['S'])
                total_sum_second = sum(tier_dict[second_player]['S'])
                if total_sum_first < total_sum_second:
                    del tier_dict[first_player]
                elif total_sum_first > total_sum_second:
                    del tier_dict[second_player]
    return tier_dict


tier = {}


while True:
    command = input()
    if command == "Season end":
        break
    if ' -> ' in command:
        current_command = command.split(' -> ')
        player, position, skill = current_command[0], current_command[1], int(current_command[2])
        if player not in tier:
            tier[player] = {'P': [], 'S': []}
            tier[player]['P'].append(position)
            tier[player]['S'].append(skill)
        else:
            if position not in tier[player]['P']:
                tier[player]['P'].append(position)
                tier[player]['S'].append(skill)
            else:
                index = tier[player]['P'].index(position)
                if tier[player]['S'][index] < skill:
                    tier[player]['S'][index] = skill
    if ' vs ' in command:
        current_command = command.split(' vs ')
        player_one, player_two = current_command[0], current_command[1]
        if player_one in tier and player_two in tier:
            tier = duel(tier, player_one, player_two)
        else:
            continue

print(tier)