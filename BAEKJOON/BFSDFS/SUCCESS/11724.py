from sys import stdin


def findAndInsert(startPoint, endPoint):
    count = 0
    length = len(result)

    for index, value in enumerate(result):
        if startPoint in value or endPoint in value:
            new_set = {startPoint, endPoint}
            result[index] = value.union(new_set)
            break
        else:
            count += 1

    if count == length:
        new_set = {startPoint, endPoint}
        result.append(new_set)


def deduplication():

    i = 0

    while i < len(result) - 1:
        for j in range(i + 1, len(result)):
            if not len(result[i].intersection(result[j])) == 0:
                result[i] = result[i] | result[j]
                result[j] = 0
        try:
            while True:
                result.remove(0)
        except ValueError:
            i += 1


N, M = map(int, stdin.readline().split())
result = []

for _ in range(M):
    S, E = map(int, stdin.readline().split())
    findAndInsert(S, E)
deduplication()

count = len(result)

for i in result:
    N -= len(i)

count += N

print(count)
