T = int(input())
for t in range(T):
    string = input()
    los, his = string.split(" ")
    lo, hi = int(los), int(his)
    prime = {}  # dictionary that contains whether a number is prime or not

    for x in range(lo, hi+1):
        # check whether x is prime or not
        if prime.get(x):
            print(x, end=" ")
        elif prime.get(x) is None:
            flag = 0
            for y in range(2, int(float(x)**0.5)+1):
                if x % y == 0:
                    flag += 1
            if flag == 0 and x != 1:
                prime[x] = True
                print(x, end=" ")
            else:
                prime[x] = False
        else:
            continue
    print()