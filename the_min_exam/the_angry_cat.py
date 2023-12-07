def cheap(prices, value, index):
    left_part = [num for num in prices[:index]]
    right_part = [num for num in prices[index::]]
    left_sum = 0
    right_sum = 0
    for num in left_part:
        if num < value:
            left_sum += num
    for num in right_part:
        if num < value:
            right_sum += num
    if left_sum >= right_sum:
        left_part = True
        final_price = left_sum
    else:
        left_part = False
        final_price = right_sum
    return left_part, final_price


def expensive(prices, value, index):
    left_part = [num for num in prices[:index]]
    right_part = [num for num in prices[index::]]
    left_sum = 0
    right_sum = 0
    for num in left_part:
        if num >= value:
            left_sum += num
    for num in right_part:
        if num >= value:
            right_sum += num
    if left_sum >= right_sum:
        left_part = True
        final_price = left_sum
    else:
        left_part = False
        final_price = right_sum
    return left_part, final_price


lst_of_price = list(map(int, input().split(', ')))
entry_point = int(input())
separate_value = lst_of_price.pop(entry_point)
type_of_items = input()
left = False
price = 0
if type_of_items == "cheap":
    left, price = cheap(lst_of_price, separate_value, entry_point)
elif type_of_items == "expensive":
    left, price = expensive(lst_of_price, separate_value, entry_point)

if left:
    position = "Left"
    print(f"{position} - {price}")
else:
    position = "Right"
    print(f"{position} - {price}")