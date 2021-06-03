from sys import stdin

dna_kind = ['A', 'C', 'G', 'T']
count, length = map(int, stdin.readline().split(" "))

## 입력을 2차원 배열로 만들기
dna_list = []
for column in range(count):
    dna_list.append(list(stdin.readline()))

result = []
## 컬럼별 가장 많이 같은 문자 찾아서 result 리스트에 저장
for column in range(length):
    max_char = ""
    max_count = 0
    for dna in dna_kind:
        char = dna
        char_count = 0
        for row in range(count):
            if (dna_list[row][column] == dna):
                char_count += 1
        if (max_count < char_count):
            max_count = char_count
            max_char = char
    result.append(max_char)

print(''.join(result))

##거리 계산
distance = 0
for row in range(count):
    for column in range(length):
        if(dna_list[row][column] != result[column]):
            distance += 1

print(distance)