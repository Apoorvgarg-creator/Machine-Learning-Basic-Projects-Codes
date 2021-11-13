N = int(input())
flag = 0
# According to the question, if the sequence once goes to increasing nature it cannot change its nature
std = True  # Assuming that series is strictly decreasing
nature = 0
for x in range(N):
    A = int(input())
    if x == 0:
        curr = A
    prev = curr
    curr = A
    if x == 0: continue
    else:
        if prev == curr:
            flag = -1
            break
        if std:
            if prev > curr:

                continue
            else:
                nature += 1
                std = False
                flag += 1
        else:
            if prev < curr:
                nature += 1
                continue
            else:
                std = True
                flag += 1

if flag == -1 or flag > 2: print("false")
elif nature == N-1: print("true")
elif flag<2:print("true")
else: print("false")
