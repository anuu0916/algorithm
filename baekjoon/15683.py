# 15683 감시
import sys
import copy
n, m = map(int, sys.stdin.readline().split())
arr = []
cctv = []  # cctv 위치 저장

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]],
    [[0, 1, 2, 3]]
]


for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    arr.append(tmp)
    for j in range(m):
        if 0 < tmp[j] < 6:
            cctv.append([tmp[j], i, j])


def watch(board, move, x, y):
    for mm in move:
        nx = x
        ny = y
        while True:
            nx += dx[mm]
            ny += dy[mm]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 6:
                    break
                elif board[nx][ny] == 0:
                    board[nx][ny] = 7
            else:
                break


def dfs(depth, office):
    global min_value

    if depth == len(cctv):
        cnt = 0
        for i in range(n):
            cnt += office[i].count(0)
        min_value = min(cnt, min_value)
        return
    
    temp = copy.deepcopy(office)
    num, x, y = cctv[depth]
    
    for mo in mode[num]:
        watch(temp, mo, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(office)
    


min_value = int(1e9)
dfs(0, arr)
print(min_value)

