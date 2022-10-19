# 2493 탑
import sys
from collections import deque
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

stack = deque([n-1])
result = [0] * n

for i in range(n-2, -1, -1):
    for j in range(len(stack)):
        if arr[i] < arr[stack[-1]]:
            break

        if arr[i] >= arr[stack[-1]]:
            num = stack.pop()
            result[num] = i + 1

    stack.append(i)

print(' '.join(map(str, result)))
