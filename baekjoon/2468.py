# 2468 안전 영역
import sys
sys.setrecursionlimit(10 ** 5)
n = int(input())
graph = list()
highest = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    if max(line) > highest:
        highest = max(line)
    graph.append(line)


def dfs(v, visited, rain):
    for k in range(4):
        nextX = v[1] + dx[k]
        nextY = v[0] + dy[k]
        if 0 <= nextX < n and 0 <= nextY < n:
            if graph[nextY][nextX] > rain and visited[nextY][nextX] == 0:
                visited[nextY][nextX] = 1
                dfs([nextY, nextX], visited, rain)


safe = 0

for r in range(highest):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > r and visited[i][j] == 0:
                visited[i][j] = 1
                dfs([i, j], visited, r)
                cnt += 1

    if cnt > safe:
        safe = cnt

print(safe)
