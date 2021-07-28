# 1012 유기농 배추
import sys
sys.setrecursionlimit(10 ** 5)
t = int(input())

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def dfs(graph, v, visited, m, n):
    for j in range(4):
        nextX = v[1] + dx[j]
        nextY = v[0] + dy[j]
        if 0 <= nextX < m and 0 <= nextY < n:
            if graph[nextY][nextX] == 1 and visited[nextY][nextX] == 0:
                visited[nextY][nextX] = 1
                dfs(graph, [nextY, nextX], visited, m, n)


for i in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    cabbage = list()
    cnt = 0

    for j in range(k):
        x, y = map(int, sys.stdin.readline().split())
        cabbage.append([y, x])
        graph[y][x] = 1

    for [y, x] in cabbage:
        if visited[y][x] == 0:
            visited[y][x] = 1
            dfs(graph, [y, x], visited, m, n)
            cnt += 1

    print(cnt)
