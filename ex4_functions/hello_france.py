import math
collections_of_items = input().split("|")
budget = int(input())
reducing_budget = budget
ticket_price = 150
lst_of_items = []
lst_of_price = []
lst_of_items_n_price = []
cost_sum = 0

[lst_of_items_n_price.append(item.split("->")) for item in collections_of_items]

for lst in lst_of_items_n_price:
    current_item = lst[0]
    current_price = float(lst[1])

    if reducing_budget < current_price:
        continue
    cost_sum += current_price
    if current_item == "Clothes" and current_price <= 50:
        reducing_budget -= current_price
        lst_of_items.append(current_item)
        lst_of_price.append(current_price * 1.4)

    elif current_item == "Shoes" and current_price <= 35:
        reducing_budget -= current_price
        lst_of_items.append(current_item)
        lst_of_price.append(current_price * 1.4)

    elif current_item == "Accessories" and current_price <= 25.5:
        reducing_budget -= current_price
        lst_of_items.append(current_item)
        lst_of_price.append(current_price * 1.4)

format_lst_of_price = ["%.2f" % price for price in lst_of_price]

print(*format_lst_of_price, sep=" ")

profit = math.fsum(lst_of_price) + reducing_budget - budget
print(f"Profit: {profit:.2f}")

final_budget = math.fsum(lst_of_price) + reducing_budget
if final_budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")