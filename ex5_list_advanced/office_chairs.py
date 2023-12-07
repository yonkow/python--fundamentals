counter = int(input())
free_chairs = 0
game_on = True
for room in range(1, counter + 1):
    chairs, visitors = input().split()
    if len(chairs) >= int(visitors):
        free_chairs += len(chairs) - int(visitors)
    else:
        needed_chairs = abs(len(chairs) - int(visitors))
        game_on = False
        print(f"{needed_chairs} more chairs needed in room {room}")

if game_on:
    print(f"Game On, {free_chairs} free chairs left")