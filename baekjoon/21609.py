# 21609 상어 중학교
from collections import deque
n, m = map(int, input().split())
arr = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, input().split())))


def find_block():
    max_group = []
    max_rainbow = 0
    blocks = []
    grouped = [[0] * n for _ in range(n)]
    # dfs
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                blocks.append([i, j, arr[i][j]])

    for b in blocks:
        if grouped[b[0]][b[1]] == 1:
            continue
        stack = deque([b])
        visited = [[0] * n for _ in range(n)]
        visited[b[0]][b[1]] = 1
        grouped[b[0]][b[1]] = 1
        color_num = arr[b[0]][b[1]]
        group = []
        rainbow = 0
        while stack:
            # print("stack", stack)
            x, y, color = stack.pop()
            group.append([x, y, color])
            # print("group", group)
            if color == 0:
                rainbow += 1
            else:
                grouped[x][y] = 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny] == 1:
                    continue
                if arr[nx][ny] != 0 and arr[nx][ny] != color_num:
                    continue
                stack.append([nx, ny, arr[nx][ny]])
                visited[nx][ny] = 1

        if len(max_group) < len(group):
            max_group = [item[:] for item in group]
            max_rainbow = rainbow
        elif len(max_group) == len(group) and max_rainbow < rainbow:
            max_group = [item[:] for item in group]
            max_rainbow = rainbow
        elif len(max_group) == len(group) and max_rainbow == rainbow:
            if (max_group[0][0] * 100 + max_group[0][1]) < (group[0][0] * 100 + group[0][1]):
                max_group = [item[:] for item in group]
                max_rainbow = rainbow

    return max_group


def gravity():
    for j in range(n):
        for i in range(n-2, -1, -1):
            if arr[i][j] == -1 or arr[i][j] == -2:
                continue

            x , y = i, j
            for k in range(1, n-i):
                nx = x + 1
                ny = y
                if arr[x][y] == -1:
                    break
                if arr[nx][ny] == -2:
                    arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                x, y = nx, ny


def print_arr():
    for i in range(n):
        print(arr[i])


score = 0
while True:
    block = find_block()
    if len(block) < 2:
        break

    score += len(block) ** 2
    for i in range(len(block)):
        x, y = block[i][0], block[i][1]
        arr[x][y] = -2

    gravity()
    arr = list(map(list, zip(*arr)))[::-1]
    gravity()

print(score)
