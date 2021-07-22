# 7576 토마토
# 문제 첫인상 : 경쟁적 전염이랑 비슷하다...
import sys
from collections import deque
m, n = map(int, sys.stdin.readline().split())
adj = {}
box = list()  # 토마토 들어있는 상자 표시할 배열
queue = deque()

for i in range(n):
    line = list(map(int, sys.stdin.readline().split()))

    # 익은 토마토가 들어있는 칸 (1인 칸)은 큐에 넣음
    # 익은 토마토 모두가 동시에 영향을 주기 때문..
    for j in range(m):
        if line[j] == 1:
            queue.append([i, j, 0])
    box.append(line)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
minDay = 0  # 최단거리 (최소 일수) 넣을 변수

while queue:
    y, x, day = queue.popleft()
    minDay = day  # 가장 마지막에 pop되는 애가 마지막에 익은거니까 계속 넣어줌

    # 상하좌우 탐색
    for i in range(4):
        row = y + dy[i]
        col = x + dx[i]
        # box 칸이 0일 때 (덜 익은 토마토일 때)만 큐에 넣어줌
        # box에서 자체적으로 방문 처리 (0이면 방문 안한 것)
        if 0 <= row < n and 0 <= col < m and box[row][col] == 0:
            box[row][col] = 1  # 토마토 익음 (방문 처리)
            queue.append([row, col, day+1])

# 덜 익은 토마토 개수 (0의 개수) 카운트
check = 0
for i in range(n):
    check += box[i].count(0)

if check == 0:
    print(minDay)
else:
    print(-1)
