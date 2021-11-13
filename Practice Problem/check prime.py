x = int(input())
flag = 0

for y in range(2, int(float(x)**0.5)+1):
    if x % y == 0:
        flag += 1

if flag == 0 and x != 1:
    print("prime")
else:
    print("not prime")