# 2740 행렬 곱셈
import sys
n, m = map(int, sys.stdin.readline().split())
a = []

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, sys.stdin.readline().split())
b = []

for i in range(m):
    b.append(list(map(int, sys.stdin.readline().split())))

result = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        tmp = 0
        for t in range(m):
            tmp += a[i][t] * b[t][j]
        result[i][j] = tmp

for i in range(n):
    print(*result[i])
