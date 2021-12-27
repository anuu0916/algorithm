# 14502 연구소
import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []
virus = []
temp = []
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
result = 0

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if tmp[j] == 2:
            virus.append([i, j])
    arr.append(tmp)


def spread_virus():
    lab = copy.deepcopy(temp)
    q = deque(virus)

    # bfs
    while q:
        y, x = q.popleft()

        # 상하좌우 이동
        for _ in range(4):
            nextY = y + dy[_]
            nextX = x + dx[_]

            if 0 <= nextY < n and 0 <= nextX < m:  # 범위 내
                if lab[nextY][nextX] == 0:  # 빈 칸이면
                    lab[nextY][nextX] = 2  # 바이러스 감염
                    q.append([nextY, nextX])  # 바이러스 큐에 추가

    zero = 0
    # 안전영역(빈 칸) 세기
    for _ in range(n):
        zero += lab[_].count(0)

    global result
    result = max(result, zero)

    return


def make_wall(cnt):
    if cnt == 3:
        spread_virus()
        return

    for k in range(n):
        for p in range(m):
            if temp[k][p] == 0:  # 빈칸을 발견하면
                temp[k][p] = 1  # 해당 칸에 벽을 세움
                make_wall(cnt+1)  # 이어서 벽 세우기
                temp[k][p] = 0  # 해당 칸에 벽을 다시 허문다


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:  # 빈칸을 발견하면
            temp = copy.deepcopy(arr)  # 지도 복사
            temp[i][j] = 1  # 해당 칸에 벽을 세움
            make_wall(1)  # 이어서 벽 세우기
            temp[i][j] = 0  # 해당 칸에 벽을 다시 허문다

print(result)
