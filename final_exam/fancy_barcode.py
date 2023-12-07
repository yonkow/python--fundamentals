import re

pattern = r"(@#+)([A-Z][a-zA-Z0-9]{4,}[A-Z])(@#+)"
number_of_lines = int(input())
for _ in range(number_of_lines):
    current_barcode = input()
    match = re.search(pattern, current_barcode)
    product_group = ''
    if match:
        digits = re.findall(r"\d+", current_barcode)
        if digits:
            for digit in digits:
                product_group += digit
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")