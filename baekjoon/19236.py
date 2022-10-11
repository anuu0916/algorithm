# 19236 청소년 상어
import copy
first_arr = []
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    tmp = list(map(int, input().split()))
    tmp_arr = []
    for j in range(0, 8, 2):
        tmp_arr.append([tmp[j], tmp[j+1]-1])
    first_arr.append(tmp_arr)


def move_fish(arr, sx, sy):
    for fish in range(1, 17):
        x = -1
        y = -1
        dir = -1

        for i in range(4):
            for j in range(4):
                if arr[i][j][0] == fish:
                    x = i
                    y = j
                    dir = arr[i][j][1]
                    break

        if x == -1 and y == -1:
            continue

        for i in range(dir, dir + 8):
            ndir = i % 8
            nx = x + dx[ndir]
            ny = y + dy[ndir]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if nx == sx and ny == sy:
                    continue
                else:
                    arr[x][y][1] = ndir
                    arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
                    break


def dfs(sx, sy, arr, cnt):
    # 물고기 먹음
    eat, sdir = arr[sx][sy][0], arr[sx][sy][1]
    arr[sx][sy][0] = -1
    cnt += eat
    global result
    result = max(result, cnt)

    # 물고기 이동
    move_fish(arr, sx, sy)

    # 다음 이동 찾기
    for i in range(1, 4):
        nx = sx + dx[sdir]*i
        ny = sy + dy[sdir]*i
        # print("next", nx, ny)
        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny][0] > 0:
            tmp = copy.deepcopy(arr)
            tmp[sx][sy] = [0, 0]
            dfs(nx, ny, tmp, cnt)


result = 0
dfs(0, 0, copy.deepcopy(first_arr), 0)
print(result)
