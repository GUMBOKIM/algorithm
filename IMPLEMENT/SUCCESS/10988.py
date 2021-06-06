from collections import deque
from sys import stdin

input = list(stdin.readline().rstrip())
length = len(input)

deque = deque(input)

while length >= 2:
    if deque.pop() != deque.popleft():
        print('0')
        break
    length -= 2

if length == 0 or length == 1:
    print('1')
