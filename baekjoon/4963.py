# 4963 섬의 개수
import sys
from collections import deque

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def dfs(graph, stack, visited, w, h):
    while stack:
        y, x = stack.pop()

        for i in range(8):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < w and 0 <= nextY < h:
                if graph[nextY][nextX] == 1 and visited[nextY][nextX] == 0:
                    visited[nextY][nextX] = 1
                    stack.append([nextY, nextX])


while True:
    w, h = map(int, sys.stdin.readline().split())
    graph = list()
    island = list()
    visited = [[0 for _ in range(w)] for _ in range(h)]
    stack = deque()
    cnt = 0

    if w == 0 and h == 0:
        break

    for i in range(h):
        line = list(map(int, sys.stdin.readline().split()))
        graph.append(line)
        for j in range(w):
            if line[j] == 1:
                island.append([i, j])

    for [y, x] in island:
        if visited[y][x] == 0:
            visited[y][x] = 1
            stack.append([y, x])
            dfs(graph, stack, visited, w, h)
            cnt += 1

    print(cnt)
