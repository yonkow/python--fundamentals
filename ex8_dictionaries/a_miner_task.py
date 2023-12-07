mined_items = {}
while True:
    command = input()
    if command == "stop":
        break
    item = command
    quantity = int(input())
    if item not in mined_items:
        mined_items[item] = 0
    mined_items[item] += quantity

for resource, quantity in mined_items.items():
    print(f"{resource} -> {quantity}")