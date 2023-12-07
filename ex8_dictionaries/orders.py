storage = {}

while True:
    command = input().split()
    if len(command) == 1:
        break
    name, price, quantity = command[0], float(command[1]), int(command[2])
    if name in storage:
        storage[name][1] += quantity
        if storage[name][0] != price:
            storage[name][0] = price
    else:
        storage[name] = []
    storage[name] += price, quantity

for product_name, quantity in storage.items():
    total_price = quantity[0] * quantity[1]
    print(f"{product_name} -> {total_price:.2f}")