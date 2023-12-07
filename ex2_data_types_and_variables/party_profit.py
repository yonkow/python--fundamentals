group_size = int(input())
adventure_days = int(input())
day_counter = 0
coin_bag = 0

while adventure_days > day_counter:
    coin_bag += 50
    day_counter += 1
    if day_counter % 15 == 0:
        group_size += 5

    if day_counter % 10 == 0:
        group_size -= 2

    if day_counter % 5 == 0:
        coin_bag += 20 * group_size
        if day_counter % 3 == 0:
            coin_bag -= 2 * group_size

    if day_counter % 3 == 0:
        coin_bag -= 3 * group_size

    coin_bag -= 2 * group_size

coin_per_companion = coin_bag // group_size
print(f"{group_size} companions received {coin_per_companion} coins each.")