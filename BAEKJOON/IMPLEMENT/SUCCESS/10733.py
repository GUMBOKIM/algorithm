from sys import stdin

count = int(stdin.readline())
account = []
for i in range(count):
    temp = int(stdin.readline())
    if temp == 0:
        account.pop()
    else:
        account.append(temp)

print(sum(account))
