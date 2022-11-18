# 1358 하키
import sys
input = sys.stdin.readline
w, h, x, y, p = map(int, input().split())
r = h // 2
cnt = 0

for i in range(p):
    cx, cy = map(int, input().split())

    # 직사각형 포함여부
    if x <= cx <= x+w and y <= cy <= y+h:
        cnt += 1
        continue

    # 반원 포함여부 : 원의 중심에서 지금 점까지의 거리와 r 비교
    d = ((cx - x)**2 + (cy-y-r)**2)**0.5
    if d <= r:
        cnt += 1
        continue
    
    d = ((cx - x - w)**2 + (cy-y-r)**2)**0.5
    if d <= r:
        cnt += 1
        continue
    
print(cnt)