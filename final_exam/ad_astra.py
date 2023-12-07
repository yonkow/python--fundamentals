import re

text_string = input()
pattern = r"(#|\|)([A-Z a-z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,})\1"

container = re.findall(pattern, text_string)
total_nutrition = 0
print_result = ""
for food in container:
    item_name, expiration_date, calories = food[1], food[2], int(food[3])
    total_nutrition += calories
    print_result += f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}\n"
days = total_nutrition // 2000
print(f"You have food to last you for: {days} days!")
print(print_result)