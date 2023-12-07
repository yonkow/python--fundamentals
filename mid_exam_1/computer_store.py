current_price = 0
taxes = 0
is_special = False
is_regular = False
while True:
    command = input()
    if command == "special":
        is_special = True
        break
    elif command == "regular":
        is_regular = True
        break
    else:
        current_price_component = float(command)
        if current_price_component < 0:
            print("Invalid price!")
        elif current_price_component == 0:
            print("Invalid order!")
        else:
            taxes += current_price_component * 0.2
            current_price += current_price_component

total_price = current_price + taxes

if is_special and total_price != 0:
    total_price *= 0.9
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {current_price:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$""")
elif is_regular and total_price != 0:
    print(f"""Congratulations you've just bought a new computer!
Price without taxes: {current_price:.2f}$
Taxes: {taxes:.2f}$
-----------
Total price: {total_price:.2f}$""")
else:
    print("Invalid order!")