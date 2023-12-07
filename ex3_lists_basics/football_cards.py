team_1 = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_2 = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
stop_condition = False
lst_of_cards = input().split()

for i, player in enumerate(lst_of_cards):

    if player in team_1:
        team_1.remove(player)
    elif player in team_2:
        team_2.remove(player)

    if len(team_1) < 7 or len(team_2) < 7:
        stop_condition = True
        break
        
if stop_condition:
    print(f"Team A - {len(team_1)}; Team B - {len(team_2)}")
    print(f"Game was terminated")
else:
    print(f"Team A - {len(team_1)}; Team B - {len(team_2)}")