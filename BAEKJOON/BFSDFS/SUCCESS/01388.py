from sys import stdin


def visitedCheck():
    if check[now[0]][now[1]] == 0:
        return False
    else:
        return True


def rowCheck():
    temp = now[:]

    while ground[temp[0]][temp[1]] == '-':
        check[temp[0]][temp[1]] = 1
        temp[0] += 1
        if temp[0] == row:
            break


def colCheck():
    temp = now[:]
    while ground[temp[0]][temp[1]] == '|':
        check[temp[0]][temp[1]] = 1
        temp[1] += 1
        if temp[1] == col:
            break


row, col = map(int, stdin.readline().split())
ground = []
for _ in range(row):
    ground.append(list(stdin.readline().strip()))

check = [[0] * col for _ in range(row)]

now = [0, 0]
count = 0

while now != [row, 0]:

    if not visitedCheck():
        count += 1
        if ground[now[0]][now[1]] == '-':
            rowCheck()
        else:
            colCheck()

    if now[1] == col - 1:
        now[0] += 1
        now[1] = 0
    else:
        now[1] += 1

print(count)
