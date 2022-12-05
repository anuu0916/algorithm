# 10845 큐
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])

for i in range(n):
    line = list(input().split())

    if line[0] == 'push':
        queue.append(int(line[1]))
    elif line[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif line[0] == 'size':
        print(len(queue))
    elif line[0] == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif line[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif line[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
