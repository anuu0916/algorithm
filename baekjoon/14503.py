# 14503 로봇 청소기
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
arr = []

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 청소한 곳은 2로 표시

cnt = 0
dir = 0
queue = deque([[r, c]])

while queue:
    r, c = queue.pop()
    # 현재 위치 청소
    if arr[r][c] == 0:
        arr[r][c] = 2
        cnt += 1
    
    if dir >= 4:
        nr = r + dr[d-2]
        nc = c + dc[d-2]
        if arr[nr][nc] != 1:
            queue.append([nr, nc])
            dir = 0
        else: 
            break
    else:
        # 왼쪽 탐색
        d -= 1
        if d < 0:
            d = 3

        nr = r + dr[d]
        nc = c + dc[d]

        if arr[nr][nc] == 0:
            queue.append([nr, nc])
            dir = 0
        else:
            queue.append([r, c])
            dir += 1

print(cnt)