# 14502 연구소 다시풀기
import sys
import copy
from collections import deque
n, m = map(int, sys.stdin.readline().split())
# 연구소
graph = []
# 바이러스 위치
virus = []
# 상하좌우 이동
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
# 결과값
result = 0

# 연구소 입력
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    # 바이러스 위치 저장
    for j in range(m):
        if tmp[j] == 2:
            virus.append([i, j])
    graph.append(tmp)


# 바이러스 퍼뜨리기
def bfs():
    tmp = copy.deepcopy(g)
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()

        # 상하좌우 이동
        for d in range(4):
            nextX = x + dx[d]
            nextY = y + dy[d]

            if 0 <= nextX < n and 0 <= nextY < m:
                if tmp[nextX][nextY] == 0:
                    tmp[nextX][nextY] = 2
                    queue.append([nextX, nextY])

    zero = 0
    # 안전영역(빈 칸) 세기
    for _ in range(n):
        zero += tmp[_].count(0)

    # 더 큰 안전 영역의 넓이 저장
    global result
    result = max(result, zero)

    return


# 벽 세우기
def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for k in range(n):
        for p in range(m):
            if g[k][p] == 0:
                g[k][p] = 1
                make_wall(cnt + 1)
                g[k][p] = 0


# 첫 번째 벽 세우기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            g = copy.deepcopy(graph)
            g[i][j] = 1
            make_wall(1)
            g[i][j] = 0

print(result)
