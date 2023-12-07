def palindrome_integer(lst_of_numbers):
    palindrome_lst = []
    for current_number in lst_of_numbers:
        if current_number == current_number[::-1]:
            palindrome_lst.append(True)
        else:
            palindrome_lst.append(False)
    return palindrome_lst


number_lst = input().split(", ")
returned_lst = palindrome_integer(number_lst)
print(*returned_lst, sep=" \n")
