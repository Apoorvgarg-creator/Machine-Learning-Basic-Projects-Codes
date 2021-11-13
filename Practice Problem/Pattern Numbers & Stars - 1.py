N = int(input())
count = 0
n = N
while count < N :
    value = 1
    for i in range(n):
        print(value, end=" ")
        value += 1
    x = 2 * count - 1
    for y in range(x):
        print("*", end=" ")
    print()
    count += 1
    n -= 1
