from sys import stdin

while True:
    mem = list(stdin.readline().rstrip().split(' '))
    if mem[0] == "0":
        break

    size = int(mem[0])
    for a in range(size - 5):
        for b in range(a + 1, size - 4):
            for c in range(b + 1, size - 3):
                for d in range(c + 1, size - 2):
                    for e in range(d + 1, size - 1):
                        for f in range(e + 1, size):
                            print(mem[a + 1], mem[b + 1], mem[c + 1], mem[d + 1], mem[e + 1], mem[f + 1])
    print("")
