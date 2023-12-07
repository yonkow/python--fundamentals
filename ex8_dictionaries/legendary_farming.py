collected_items = {'shards': 0, 'fragments': 0, 'motes': 0}
is_obtained = False
while True:
    farming = input().split()
    for index in range(0, len(farming), 2):
        item = farming[index + 1].lower()
        if item not in collected_items:
            collected_items[item] = 0
        collected_items[item] += int(farming[index])
        if collected_items["shards"] >= 250:
            print(f"Shadowmourne obtained!")
            collected_items["shards"] -= 250
            is_obtained = True
        elif collected_items["fragments"] >= 250:
            print(f"Valanyr obtained!")
            collected_items["fragments"] -= 250
            is_obtained = True
        elif collected_items["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            collected_items["motes"] -= 250
            is_obtained = True
        if is_obtained:
            break
    if is_obtained:
        break

for material, quantity in collected_items.items():
    print(f"{material}: {quantity}")