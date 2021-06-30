import sys

sys.setrecursionlimit(10000)
N, M = map(int, sys.stdin.readline().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(v):
    visited[v] = True
    for i in range(1, N + 1):
        if not visited[i] and graph[v][i] == 1:
            dfs(i)


for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
