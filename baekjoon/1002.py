# 1002 터렛
import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue

    d = ((x1-x2)**2 + (y1-y2)**2)
    rsum = (r1+r2)**2
    
    # 교점 X (외부)
    if rsum < d:
        print(0)
    # 한 점에서 접함 (외접)
    elif rsum == d:
        print(1)
    # 한 점에서 접함 (내접)
    elif (r1-r2)**2 == d:
        print(1)
    # 교점 X (내부)
    elif (r1-r2)**2 > d:
        print(0)
    # 교점 2개
    elif rsum > d:
        print(2)
