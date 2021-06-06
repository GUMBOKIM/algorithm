from sys import stdin

people_count = int(stdin.readline())
people_list = list(map(int, stdin.readline().split(" ")))

people_list.sort()

result = 0
for index, value in enumerate(people_list):
    result += value * (people_count - index)

print(result)