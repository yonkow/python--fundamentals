def next_version(current):
    current[-1] += 1
    if current[-1] > 9:
        current[-1] = 0
        current[1] += 1
        if current[1] > 9:
            current[1] = 0
            current[0] += 1
    return current


current_version = [int(num) for num in input().split(".")]
next_ver = next_version(current_version)
print('.'.join(str(num) for num in next_ver))