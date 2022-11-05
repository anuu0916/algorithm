# 10026 적록색약
import sys
from collections import deque
n = int(input())
arr = []

for i in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

queue = deque([(0,0)])
visited = [[0] * n for _ in range(n)]
visited[0][0] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
cnt_color = 0
cnt_normal = 0

while queue:
    # print(queue)
    x, y = queue.popleft()
    color = arr[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if color == arr[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    if len(queue) == 0:
        # print("null")
        cnt_normal += 1
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
                    break
            if len(queue) > 0:
                break

queue = deque([(0,0)])
visited = [[0] * n for _ in range(n)]
visited[0][0] = 1

while queue:
    x, y = queue.popleft()
    color = arr[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            if color == 'B' and color == arr[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
            if color != 'B' and arr[nx][ny] != 'B':
                visited[nx][ny] = 1
                queue.append((nx, ny))
    
    if len(queue) == 0:
        cnt_color += 1
        for i in range(n):
            for j in range(n):
                if visited[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = 1
                    break
            if len(queue) > 0:
                break

print(cnt_normal, cnt_color)
