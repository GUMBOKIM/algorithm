from sys import stdin

case = 1

while True:
    L, P, V = map(int, stdin.readline().split(" "))

    if L == 0:
        break

    quotient, remainder = divmod(V, P)

    if remainder <= L:
        count = quotient * L + remainder
    else:
        count = quotient * L + L

    print("Case " + str(case) + ": " + str(count))
    case += 1
