def positive(numbers: list):
    positive_lst = [num for num in numbers if num >= 0]
    return positive_lst


def negative(numbers: list):
    negative_lst = [num for num in numbers if num < 0]
    return negative_lst


def even(numbers: list):
    even_lst = [num for num in numbers if num % 2 == 0]
    return even_lst


def odd(numbers: list):
    odd_lst = [num for num in numbers if num % 2 != 0]
    return odd_lst


nums = [int(num) for num in input().split(', ')]
positive_nums = positive(nums)
negative_nums = negative(nums)
even_nums = even(nums)
odd_nums = odd(nums)

print(f"""Positive: {', '.join(str(num) for num in positive_nums)}
Negative: {', '.join(str(num) for num in negative_nums)}
Even: {', '.join(str(num) for num in even_nums)}
Odd: {', '.join(str(num) for num in odd_nums)}""")