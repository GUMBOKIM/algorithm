from collections import deque
from sys import stdin

computer_cnt = int(stdin.readline())
pair = int(stdin.readline())

graph = [[0] * (computer_cnt + 1) for i in range(computer_cnt + 1)]

for i in range(pair):
    m1, m2 = map(int, input().split())
    # 노드 연결 하기
    graph[m1][m2] = graph[m2][m1] = 1


# 너비 우선 탐색
def bfs(value):
    find = [value]
    # deque 생성
    queue = deque()
    queue.append(value)

    while queue:
        v = queue.popleft()

        for w in range(len(graph[value])):
            if graph[v][w] == 1 and (w not in find):
                find.append(w)
                queue.append(w)

    return find


print(len(bfs(1)) - 1)