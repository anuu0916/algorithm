# 10828 스택
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
stack = deque([])

for i in range(n):
    line = list(input().split())

    if line[0] == 'push':
        stack.append(int(line[1]))
    elif line[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif line[0] == 'size':
        print(len(stack))
    elif line[0] == 'empty':
        if len(stack) > 0:
            print(0)
        else:
            print(1)
    elif line[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
