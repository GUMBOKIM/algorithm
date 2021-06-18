from sys import stdin

## 1
## 2

## 3

## 4

size = int(stdin.readline())
grid = []
for i in range(size):
    grid.append(list(map(int, stdin.readline().split(" "))))

print(grid)