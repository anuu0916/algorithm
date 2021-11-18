# 1026 보물
import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
# sorted_B = sorted(B, reverse=True)

result = 0
for i in range(n):
    # result += A[i] * sorted_B[i]
    result += A[i] * B.pop(B.index(max(B)))

print(result)
