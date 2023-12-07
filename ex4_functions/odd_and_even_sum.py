def odd_and_even(number: str):
    odd_sum_digits = 0
    even_sum_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum_digits += int(digit)
        else:
            odd_sum_digits += int(digit)
    return odd_sum_digits, even_sum_digits


inserted_number = input()
odd_sum, even_sum = odd_and_even(inserted_number)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")