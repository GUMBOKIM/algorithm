from sys import stdin

N, M, k = map(int, stdin.readline().split(" "))

grid_shark = []
for i in range(N):
    grid_shark.append(list(map(int, stdin.readline().split(" "))))

grid_scent = []
for i in range(N):
    for j in range(N):
        if grid_shark[i][j] == 0:
            grid_scent[i][j] = 0
        else:
            grid_scent[i][j] = k

shark_dir = []
shark_dir.append(list(map(int, stdin.readline().split(" "))))

shark_rule = []
for i in range(M):
    shark_rule.append(list(map(int, stdin.readline().split(" "))))

