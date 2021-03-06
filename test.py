from sys import stdin

case = 1

while L != 0:
    L, P, V = map(int, stdin.readline().split(" "))

    quotient, remainder = divmod(V, P)

    if remainder <= L:
        count = quotient * L + remainder
    else:
        count = quotient * L + L

    print("Case " + str(case) + ": " + str(count))
    case += 1
