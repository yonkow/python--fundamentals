def sorted_lst(inserted_lst: list):
    sorted_number = sorted(inserted_lst)
    return sorted_number


number_lst = input().split()
number_lst = list(map(int, number_lst))
print(sorted_lst(number_lst))

# Съкратен начин без финкция
# number_lst = input().split()
# number_lst = list(map(int, number_lst))
# print(sorted(number_lst))