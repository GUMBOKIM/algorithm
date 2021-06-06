from sys import stdin

## 입력하기
N, M, B = map(int, stdin.readline().split(" "))

ground = []
for i in range(N):
    ground += list(map(int, stdin.readline().split(" ")))

## 시작 층수(최소값), 최고 층수 계산하기
floor_min = min(ground)
floor_max = min(256, (sum(ground) + B) // (N * M))

result = []
for floor in range(floor_min, floor_max + 1):
    time = 0
    for sel in ground:
        temp = floor - sel
        if temp > 0:
            time += temp
        elif temp < 0:
            time -= 2 * temp
    result.append([time, floor])
result.sort(key=lambda x: [x[0], -x[1]])

print(result[0][0], result[0][1])
