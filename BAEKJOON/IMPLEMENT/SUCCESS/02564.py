from sys import stdin


## XY좌표로 변환
def convertXY(map):
    side, length = map
    global h, w
    if side == 1:
        return [side, length, h]
    if side == 2:
        return [side, length, 0]
    if side == 3:
        return [side, 0, h - length]
    if side == 4:
        return [side, w, h - length]

## 거리 계산
def calculateDistance(my_location, store):
    global h, w
    """
    건너편인 경우
    my_location[0] == 1 and store[0] == 2
    my_location[0] == 2 and store[0] == 1
    my_location[0] == 3 and store[0] == 4
    my_location[0] == 4 and store[0] == 3
    """
    if (my_location[0] == 1 and store[0] == 2) or (my_location[0] == 2 and store[0] == 1):
        sum = my_location[1] + store[1]
        if w > sum:
            return sum + h
        else:
            return 2 * w - sum + h
    elif (my_location[0] == 3 and store[0] == 4) or (my_location[0] == 4 and store[0] == 3):
        sum = my_location[2] + store[2]
        if h > sum:
            return sum + w
        else:
            return 2 * h - sum + w
    else:
        return abs(my_location[1] - store[1]) + abs(my_location[2] - store[2])


## 입력하기
w, h = map(int, stdin.readline().split(" "))
store_count = int(stdin.readline())

store_list = []
for i in range(store_count):
    store_list.append(convertXY(map(int, stdin.readline().split(" "))))

my_location = convertXY(map(int, stdin.readline().split(" ")))

distance = 0
for store in store_list:
    distance += calculateDistance(my_location, store)

print(distance)

