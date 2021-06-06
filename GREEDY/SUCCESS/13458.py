from sys import stdin

location_count = int(stdin.readline())
location_list = list(map(int, stdin.readline().split(" ")))
conjugator, sub_conjugator = map(int, stdin.readline().split(" "))

count = 0
for location in location_list:
    location -= conjugator
    count += 1
    if location > 0:
        count += location // sub_conjugator
        if location % sub_conjugator != 0:
            count += 1

print(count)
