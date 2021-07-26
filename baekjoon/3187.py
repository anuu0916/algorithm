# 3187 양치기 꿍
import sys
from collections import deque
r, c = map(int, sys.stdin.readline().split())
fence = list()
animal = list()
cnt = 0

for i in range(r):
    fence.append(list(sys.stdin.readline().rstrip()))
    for j in range(c):
        if fence[i][j] == 'v' or fence[i][j] == 'k':
            cnt += 1
            animal.append((i, j))

visited = [[0 for _ in range(c)] for _ in range(r)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
stack = deque()
check = 0
sheep = 0
wolf = 0

while check < cnt:
    s = 0
    w = 0

    for node in animal:
        if visited[node[0]][node[1]] == 0:
            stack.append(node)
            visited[node[0]][node[1]] = 1
            break

    while stack:
        y, x = stack.pop()
        if fence[y][x] == 'v':
            w += 1
            check += 1
        elif fence[y][x] == 'k':
            s += 1
            check += 1

        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < c and 0 <= nextY < r:
                if fence[nextY][nextX] != '#' and visited[nextY][nextX] == 0:
                    visited[nextY][nextX] = 1
                    stack.append([nextY, nextX])

    if s > w:
        sheep += s
    else:
        wolf += w

print(sheep, wolf)
