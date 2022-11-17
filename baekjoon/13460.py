# 13460 구슬 탈출 2
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
goal = ()
rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    tmp = list(input().rstrip())
    arr.append(tmp)
    for j in range(m):
        if tmp[j] == 'R':
            rx, ry = i, j
        if tmp[j] == 'B':
            bx, by = i, j
        if tmp[j] == 'O':
            goal = (i, j)


queue = deque([(rx, ry, bx, by, 0)])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = -1
visited = []
visited.append((rx, ry, bx, by))

while queue:
    rx, ry, bx, by, cnt = queue.popleft()

    if cnt > 10:
        break

    if (rx, ry) == goal:
        result = cnt
        break
    
    for i in range(4):
        nrx, nry= rx, ry

        while True:
            nrx += dx[i]
            nry += dy[i]

            if arr[nrx][nry] == '#':
                nrx -= dx[i]
                nry -= dy[i]
                break
            if arr[nrx][nry] == 'O':
                break
        
        nbx, nby = bx, by

        while True:
            nbx += dx[i]
            nby += dy[i]

            if arr[nbx][nby] == '#':
                nbx -= dx[i]
                nby -= dy[i]
                break
            if arr[nbx][nby] == 'O':
                break
        
        if (nbx, nby) == goal:
            continue

        if nrx == nbx and nry == nby: # 두 구슬의 위치가 같다면
            if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by): # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                nrx -= dx[i]
                nry -= dy[i]
            else:
                nbx -= dx[i]
                nby -= dy[i]

        if (nrx, nry, nbx, nby) not in visited:
            visited.append((nrx, nry, nbx, nby))
            queue.append([nrx, nry, nbx, nby, cnt+1])
        

print(result)
