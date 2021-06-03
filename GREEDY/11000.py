from sys import stdin

class_list = []
for i in range(int(stdin.readline())):
    class_list.append(map(int, stdin.readline().split(" ")))

print(len(class_list))


