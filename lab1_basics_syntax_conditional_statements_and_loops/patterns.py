# n = int(input())
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()
# for i in range(n - 1, 0, -1):
#     for j in range(0, i):
#         print("*", end="")
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end="*")
#     print()

n = int(input())
for i in range(n):
    for j in range(1, n-i):
        print(" ", end="")
    for k in range(1, i+2):
        print("*", end="")
    print()