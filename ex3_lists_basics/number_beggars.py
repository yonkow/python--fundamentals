collection_lst = input().split(", ")
numbers_of_beggars = int(input())
sum_of_each_beggars = []

for turns in range(numbers_of_beggars):
    current_money = 0

    for money in collection_lst[turns::numbers_of_beggars]:
        current_money += int(money)

    sum_of_each_beggars.append(current_money)

print(sum_of_each_beggars)