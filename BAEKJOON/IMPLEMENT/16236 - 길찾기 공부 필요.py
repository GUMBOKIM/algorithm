from sys import stdin


## 사이즈 작은 물고기 찾기 - 확인 완료
def findFish():
    fish_list = []
    for row in range(size):
        for col in range(size):
            if fish_grid[row][col] != 0:
                fish_list.append([row, col])
    return fish_list


## 물고기가 움직일 수 있는지 없는지 !!!
def moveableCheck(check_fish):
    return True



## 가장 가까운 물고기 선택
def selectFish(input_list):
    distance = 40
    for f in input_list:
        temp = abs(shark_info[1] - f[0]) + abs(shark_info[2] - f[1])
        if temp < distance:
            if moveableCheck(f):
                distance = temp
                select_fish = f
    return select_fish


## 움직임 계산
def moveFish(fish_input):
    row = fish_input[0]
    col = fish_input[1]
    distance = abs(shark_info[1] - row) + abs(shark_info[2] - col)
    shark_info[1] = row
    shark_info[2] = col
    shark_info[3] += 1
    fish_grid[row][col] = 0
    return distance


## 상어 진화
def evolutionCheck():
    if shark_info[0] == shark_info[3]:
        shark_info[0] += 1
        shark_info[3] = 0


########## 그리드 보여주는 함수
def showGrid():
    for row in range(size):
        print(fish_grid[row])


################### 입력
size = int(stdin.readline())
fish_grid = []
for i in range(size):
    fish_grid.append(list(map(int, stdin.readline().split(" "))))

## 상어 위치 찾기
for row in range(size):
    for col in range(size):
        if fish_grid[row][col] == 9:
            fish_grid[row][col] = 0
            ## 상어정보 만들기(크기, row, col, yummy)
            shark_info = [2, row, col, 0]

## 찾기 로직
count = 0
while True:
    fish_list = findFish()
    if len(fish_list) == 0:
        print(count)
        break
    else:
        fish = selectFish(fish_list)
        print(fish)
        count += moveFish(fish)
        evolutionCheck()
