T = int(input())

for x in range(T):

    A = int(input())
    Af = int(float(A)**0.5)
    list1 = list(range(0, Af+1))
    list1.reverse()
    for y in list1:
        b = y
        asq = A - int(b)**2
        a = int(float(asq)**0.5)
        if a <= b and int(a)**2 + int(b)**2 == A:
            print("(", end="")
            print(a, end="")
            print(",", end="")
            print(b, end="")
            print(")", end="")
            print(end=" ")

    print()
