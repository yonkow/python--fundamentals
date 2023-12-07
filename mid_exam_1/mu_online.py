def potion(health_bar: int, heal: int):
    lost_health = 100 - health_bar
    if lost_health < heal:
        print(f"You healed for {lost_health} hp.")
        health_bar = 100
    elif lost_health >= heal:
        print(f"You healed for {heal} hp.")
        health_bar += heal
    print(f"Current health: {health_bar} hp.")
    return health_bar


def chest(wallet: int, bitcoins: int):
    if bitcoins >= 0:
        wallet += bitcoins
        print(f"You found {bitcoins} bitcoins.")
    return wallet


def monster_attack(health_bar: int, monster: str, damage: int):
    if damage >= 0:
        health_bar -= damage
    if health_bar > 0:
        print(f"You slayed {monster}.")
    return health_bar, monster


health = 100
bag = 0
room_counter = 0
died = False
dungeon_rooms = [room for room in input().split("|")]
for current_room in dungeon_rooms:
    room_counter += 1
    command, value = current_room.split()
    current_value = int(value)
    if command == "potion":
        health = potion(health, current_value)
    elif command == "chest":
        bag = chest(bag, current_value)
    else:
        health, current_monster = monster_attack(health, command, current_value)

    if health <= 0:
        print(f"You died! Killed by {current_monster}.")
        print(f"Best room: {room_counter}")
        died = True
        break
    else:
        pass

if not died:
    print(f"""You've made it!
Bitcoins: {bag}
Health: {health}""")