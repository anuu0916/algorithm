# 17298 오큰수
import sys
from collections import deque
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

stack = deque([0])
result = [-1] * n

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        result[stack.pop()] = arr[i]
    stack.append(i)

print(*result)
