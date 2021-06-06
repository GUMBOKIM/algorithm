from sys import stdin


count = int(stdin.readline())
rope_list = []
for i in range(count):
    rope_list.append(int(stdin.readline()))

rope_list.sort()

result = 0
for index, value in enumerate(rope_list):
    max = (count - index) * value
    if max > result:
        result = max

print(result)