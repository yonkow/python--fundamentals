budget = float(input())
flour_price = float(input())
price_per_eggs_pack = flour_price * 0.75
price_per_litter_of_milk = flour_price * 1.25
eggs_counter = 0
loaf_counter = 0
price_for_a_bread = flour_price + price_per_eggs_pack + (price_per_litter_of_milk * 0.25)

while budget > price_for_a_bread:
    budget -= price_for_a_bread
    loaf_counter += 1
    eggs_counter += 3
    if loaf_counter % 3 == 0:
        eggs_counter -= (loaf_counter - 2)
    else:
        continue
print(f"You made {loaf_counter} loaves of Easter bread! Now you have {eggs_counter} eggs and {budget:.2f}BGN left.")