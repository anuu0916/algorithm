# 14502 연구소
import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = []  # 연구소 지도
virus = []  # 바이러스의 위치를 저장할 배열
temp = []  # 벽을 세우고 허물 때 쓸 임시 지도 배열
# 상하좌우 이동
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
# 결과값
result = 0

# 연구소 지도 입력
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    # 바이러스의 위치 저장
    for j in range(m):
        if tmp[j] == 2:
            virus.append([i, j])
    arr.append(tmp)


# 바이러스 퍼뜨리기
def spread_virus():
    lab = copy.deepcopy(temp)  # 지도 복사
    q = deque(virus)  # 바이러스 위치 큐 삽입

    # bfs
    while q:
        y, x = q.popleft()  # 바이러스 위치 pop

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

    # 더 큰 안전 영역의 넓이 저장
    global result
    result = max(result, zero)

    return


# 벽 세우기
# cnt : 벽의 개수
def make_wall(cnt):
    # 벽을 다 세웠으면 바이러스 퍼뜨려보기
    if cnt == 3:
        spread_virus()
        return

    # 벽 3개를 다 안 세웠을 때
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
