def average(numbers: list):
    average_value = sum(numbers) / len(numbers)
    return average_value


def top_five(numbers: list):
    average_value = average(numbers)
    # len_of_lst = len(numbers) // 2
    top_nums = []
    while len(numbers) > 0:
        current_max = max(numbers)
        if current_max > average_value:
            top_nums.append(current_max)
        numbers.remove(current_max)
        if len(top_nums) >= 5:
            break
    return top_nums


lst_of_ints = list(map(int, input().split()))
top = top_five(lst_of_ints)
top.sort(reverse=True)
if len(top) == 0:
    print("No")
else:
    print(' '.join([str(num) for num in top]))