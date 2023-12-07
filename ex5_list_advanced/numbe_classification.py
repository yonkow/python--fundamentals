lst_of_numbers = input().split(", ")
positive = [number for number in lst_of_numbers if int(number) >= 0]
negative = [number for number in lst_of_numbers if int(number) < 0]
even = [number for number in lst_of_numbers if int(number) % 2 == 0]
odd = [number for number in lst_of_numbers if int(number) % 2 != 0]
print(f"Positive: {', '.join(str(number) for number in positive)}")
print(f"Positive: {', '.join(str(number) for number in negative)}")
print(f"Positive: {', '.join(str(number) for number in even)}")
print(f"Positive: {', '.join(str(number) for number in odd)}")