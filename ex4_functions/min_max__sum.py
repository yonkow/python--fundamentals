def min_max_sum(inserted_lst: list):
    min_num = min(inserted_lst)
    max_num = max(inserted_lst)
    summary = sum(inserted_lst)
    return min_num, max_num, summary


numbers_lst = input().split()
numbers_lst = list(map(int, numbers_lst))
print(f"The minimum number is {min_max_sum(numbers_lst)[0]}\n"
      f"The maximum number is {min_max_sum(numbers_lst)[1]}\n"
      f"The sum number is: {min_max_sum(numbers_lst)[2]}")