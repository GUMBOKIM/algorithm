from sys import stdin

meeting = int(stdin.readline())
meeting_list = []
for i in range(meeting):
    meeting_list.append(list(map(int, stdin.readline().split(" "))))

meeting_list.sort(key=lambda x: (-x[0], -x[1]))
print(meeting_list)

mem = meeting_list[-1]
count = 1
for meeting in meeting_list:
    print(meeting)
    if meeting[1] <= mem[1]:
        if meeting[1] <= mem[0]:
            mem = meeting
            count += 1
            print(mem)

