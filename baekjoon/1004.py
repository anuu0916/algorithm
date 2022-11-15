# 1004 어린 왕자
import sys
t = int(sys.stdin.readline())

def check_inside(x, y, cx, cy, r):
    if (x-cx)*(x-cx) + (y-cy)*(y-cy) <= r*r:
        return True
    else:
        return False


for test_case in range(t):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())

    cnt = 0
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        if check_inside(x1, y1, cx, cy, r) and not check_inside(x2, y2, cx, cy, r):
            cnt += 1
        elif not check_inside(x1, y1, cx, cy, r) and check_inside(x2, y2, cx, cy, r):
            cnt += 1
    
    print(cnt)
