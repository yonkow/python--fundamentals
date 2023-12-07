def multiplier(first, second):
    total = 0
    if len(first) == len(second):
        for index in range(len(first)):
            total += ord(first[index]) * ord(second[index])
    elif len(first) > len(second):
        for index in range(len(second)):
            total += ord(first[index]) * ord(second[index])
        for index in range(len(second), len(first)):
            total += ord(first[index])
    else:
        for index in range(len(first)):
            total += ord(first[index]) * ord(second[index])
        for index in range(len(first), len(second)):
            total += ord(second[index])
    return total


first_word, second_word = input().split()
total_sum = multiplier(first_word, second_word)
print(total_sum)