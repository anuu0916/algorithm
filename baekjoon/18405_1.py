# 18405 경쟁적 전염 다시풀기
import sys
from collections import deque
n, k = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

print(arr)
