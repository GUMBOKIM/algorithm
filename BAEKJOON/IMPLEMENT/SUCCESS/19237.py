from sys import stdin


# 향 지우기 - 잘됨
def decreaseScent():
    for row in range(N):
        for col in range(N):
            scent = grid_scent[row][col]
            if scent[0] != 0:
                if scent[1] == 1:
                    grid_scent[row][col] = [0, 0]
                else:
                    grid_scent[row][col][1] -= 1


# 상어 움직이기
def moveShark():
    for key, value in enumerate(shark_list):
        if value[0] == 1:
            dir_now = value[1]
            row = value[2]
            col = value[3]
            dir_list = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
            now_rule = shark_rule[key][dir_now - 1]

            ## 상어가 움직일 수 있는 공간 Count
            moveable_count = 0
            ## 상어가 냄새가 존재해 못이동하는 칸 Count
            scent_count = 0

            ## 빈칸으로 이동
            for prefer in now_rule:
                ## 격자 내부인지
                move = dir_list[prefer - 1]
                if N > move[0] >= 0 and N > move[1] >= 0:
                    moveable_count += 1
                    if grid_scent[move[0]][move[1]] == [0, 0]:
                        shark_list[key][1] = prefer
                        shark_list[key][2] = move[0]
                        shark_list[key][3] = move[1]
                        break
                    else:
                        scent_count += 1

            ## 모든공간에 냄새가 존재할때 이동
            if scent_count == moveable_count:
                for prefer in now_rule:
                    move = dir_list[prefer - 1]
                    if N > move[0] >= 0 and N > move[1] >= 0:
                        if grid_scent[move[0]][move[1]][0] == key + 1:
                            shark_list[key][1] = prefer
                            shark_list[key][2] = move[0]
                            shark_list[key][3] = move[1]
                            break


# 겹친 상어 죽이기
def deleteShark():
    for i in range(M):
        i_shark = shark_list[i]
        if i_shark[0] == 1:
            for j in range(i + 1, M):
                j_shark = shark_list[j]
                if j_shark[0] == 1:
                    if i_shark[2] == j_shark[2] and i_shark[3] == j_shark[3]:
                        shark_list[j][0] = 0


# 향 뿌리기
def createScent():
    for key, value in enumerate(shark_list):
        if value[0] == 1:
            row = value[2]
            col = value[3]
            grid_scent[row][col] = [key + 1, k]


def countShark():
    shark_count = 0
    for key, value in enumerate(shark_list):
        if value[0] == 1:
            shark_count += 1
    return shark_count


## 입력(격자, 상어, 냄새)
N, M, k = map(int, stdin.readline().split(" "))

## 상어(상태, 방향, 위치ROW, 위치COL)
shark_list = [[0] for col in range(M)]

## 입력
for row in range(N):
    grid_temp = list(map(int, stdin.readline().split(" ")))
    for col in range(N):
        temp = grid_temp[col]
        if temp != 0:
            shark_list[temp - 1] = [1, 0, row, col]

for index, value in enumerate(list(map(int, stdin.readline().split(" ")))):
    shark_list[index][1] = value

shark_rule = []
for i in range(M):
    temp_list = []
    for j in range(4):
        temp_list.append(list(map(int, stdin.readline().split(" "))))
    shark_rule.append(temp_list)

grid_scent = [[[0, 0] for col in range(N)] for row in range(N)]

count = 0
createScent()
while count <= 1000:
    count += 1
    moveShark()
    decreaseScent()
    deleteShark()
    createScent()
    if countShark() == 1:
        print(count)
        break
    if count >= 1000:
        print("-1")
        break