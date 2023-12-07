import re

pattern = r">>([a-zA-Z]{1,})<<([0-9]+[\.]?[0-9]*)!([0-9]*)"
total_cost = 0
bought_furniture = []
while True:
    command = input()
    if command == "Purchase":
        break
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_cost += float(price) * int(quantity)

print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
