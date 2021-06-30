from sys import stdin

N = int(stdin.readline())
grid = []
result = []

for i in range(N):
    grid.append(list(stdin.readline().rstrip()))


def visited(row, col):
    grid[row][col] = '0'
    count = 1
    # 위
    if row - 1 >= 0 and grid[row - 1][col] == '1':
        count += visited(row - 1, col)

    # 위
    if row + 1 < N and grid[row + 1][col] == '1':
        count += visited(row + 1, col)
    # 왼쪽
    if col - 1 >= 0 and grid[row][col - 1] == '1':
        count += visited(row, col - 1)
    # 오른쪽
    if col + 1 < N and grid[row][col + 1] == '1':
        count += visited(row, col + 1)

    return count


for R in range(N):
    for C in range(N):
        if grid[R][C] == '1':
            cnt = visited(R, C)
            result.append(cnt)
result.sort()

print(len(result))
for i in result:
    print(i)
