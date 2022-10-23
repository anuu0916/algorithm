# 7569 토마토
import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().split())
arr = []
dh = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
queue = deque([])
empty = 0

for i in range(h):
    box = []
    for j in range(n):
        tmp = list(map(int, sys.stdin.readline().split()))
        box.append(tmp)
        for k in range(m):
            if tmp[k] == 1:
                queue.append((i, j, k, 0))
            elif tmp[k] == -1:
                empty += 1
    arr.append(box)

result = 0
t_cnt = 0
while queue:
    ch, cx, cy, cnt = queue.popleft()
    t_cnt += 1
    for i in range(6):
        nh = ch + dh[i]
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nh < h and 0 <= nx < n and 0 <= ny < m:
            if arr[nh][nx][ny] == 0:
                result = cnt+1
                queue.append((nh, nx, ny, cnt+1))
                arr[nh][nx][ny] = 1

goal = h*n*m - empty
if t_cnt < goal:
    print(-1)
else:
    print(result)
