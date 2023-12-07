elements = input().split()
print(elements)
key = {item for item in elements[::2]}
value = {int(item) for item in elements[1::2]}
print(key)
