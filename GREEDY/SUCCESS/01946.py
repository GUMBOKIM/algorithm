from sys import stdin


## input은 List, index 비교 시작 부분
def compareListRank(list, index):
    init = len(list)
    list_new = []
    if init <= index + 1:
        print(init)
    else:
        for i in range(init):
            if i <= index:
                list_new.append(list[i])
            else:
                if list[index][1] > list[i][1]:
                    list_new.append(list[i])
        compareListRank(list_new, index + 1)


test_count = int(stdin.readline())

for test in range(test_count):
    applicant_count = int(stdin.readline())

    ## 서류 점수, 면접 점수 받아오기
    rank_list = []
    for i in range(applicant_count):
        rank_list.append(list(map(int, stdin.readline().split(" "))))

    ## 서류 등수 기준으로 정렬
    rank_list.sort(key=lambda rank: rank[0])

    ## 비교하기
    compareListRank(rank_list, 0)