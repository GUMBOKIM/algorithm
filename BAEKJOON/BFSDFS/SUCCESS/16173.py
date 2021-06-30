
from sys import stdin

#
# 1. ‘쩰리’는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. ‘쩰리’가 정사각형 구역의 외부로 나가는 경우엔 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
# 2. ‘쩰리’의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
# 3. ‘쩰리’가 이동 가능한 방향은 오른쪽과 아래 뿐이다. 위쪽과 왼쪽으로는 이동할 수 없다.
# 4. ‘쩰리’가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 ‘쩰리’의 승리로 게임은 종료된다.
# 5. ‘쩰리’가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다. 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.

size = int(stdin.readline())
grid = []
for i in range(size):
    grid.append(list(map(int, stdin.readline().split())))

check = [[0] * size for i in range(size)]

find = [[0, 0]]
dx = [1,0]
dy = [0,1]

while find:

    x = find[0][0]
    y = find[0][1]

    del find[0]

    move = grid[x][y]

    if move == -1:
        print("HaruHaru")
        exit(0)

    for i in range(2):
        now_x = x + dx[i] * move
        now_y = y + dy[i] * move
        if 0 <= now_x < size and 0 <= now_y < size and check[now_x][now_y] == 0:
            check[now_x][now_y] = 1
            find.append([now_x, now_y])

print("Hing")
