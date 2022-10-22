# 17836 공주님을 구해라!
import sys
from collections import deque
n, m, t = map(int, sys.stdin.readline().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)


def get_gram():
    queue = deque([(0, 0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        x, y, cnt = queue.popleft()
        if arr[x][y] == 2:
            queue = deque([(x, y, cnt)])
            visited = [[0] * m for _ in range(n)]
            visited[0][0] = 1
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != 1 and visited[nx][ny] == 0:
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1

    while queue:
        x, y, cnt = queue.popleft()
        if x == (n-1) and y == (m-1):
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1

    return int(1e5)


def no_gram():
    queue = deque([(0, 0, 0)])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        x, y, cnt = queue.popleft()
        if x == (n-1) and y == (m-1):
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0 and visited[nx][ny] == 0:
                    queue.append((nx, ny, cnt+1))
                    visited[nx][ny] = 1

    return int(1e5)


res1 = get_gram()
res2 = no_gram()
result = min(res1, res2)
if result > t:
    print("Fail")
else:
    print(result)
