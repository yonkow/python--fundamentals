needed_exp = float(input())
count_of_battle = int(input())
collected_exp = 0
battle_counter = 0
flag = False
for battle in range(1, count_of_battle + 1):
    battle_exp = float(input())
    battle_counter = battle
    if battle % 3 == 0:
        battle_exp *= 1.15
    if battle % 5 == 0:
        battle_exp *= 0.9
    if battle % 15 == 0:
        battle_exp *= 1.05
    collected_exp += battle_exp
    if collected_exp >= needed_exp:
        flag = True
        break

if flag:
    print(f"Player successfully collected his needed experience for {battle_counter} battles.")
else:
    difference = needed_exp - collected_exp
    print(f"Player was not able to collect the needed experience, {difference:.2f} more needed.")