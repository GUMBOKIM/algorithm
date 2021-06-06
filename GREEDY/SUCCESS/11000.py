from sys import stdin

class_list = []


for i in range(int(stdin.readline())):
    start, end = map(stdin.readline().split(" "))
    if i==0:
        min = start
        max = end
        for i in range(start - end):
            class_list.append(1)
    else:
        count = end - start
        if min > start:
            min = start
        if max < end:
            max = end
        for i in range(start, end):
            class_list.append(i)

     print(class_list)


