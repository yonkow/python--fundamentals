def perfect_number(num: int):
    divisor_lst = []
    for divisor in range(1 , num):
        if num % divisor == 0:
            divisor_lst.append(divisor)
    if sum(divisor_lst) == num:
        return "We have a perfect number!"
    return "It's not so perfect."


current_number = int(input())
print(perfect_number(current_number))