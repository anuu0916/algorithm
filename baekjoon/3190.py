# 3190 뱀
import sys
n = int(input())
k = int(input())
# 맵 정보
data = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
# 방향 전환 정보
info = []
# 처음에 오른쪽을 보고 있으므로 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 사과가 있는 곳은 1로 표시
for i in range(k):
    a, b = map(int, sys.stdin.readline().split())
    data[a][b] = 1

l = int(input())

for i in range(l):
    x, c = sys.stdin.readline().split()
    info.append((int(x), c))

def turn(direction, c):
    # 왼쪽으로 90도 회전
    if c == "L":
        direction = (direction - 1) % 4
    # 오른쪽으로 90도 회전
    else:
        direction = (direction + 1) % 4
    
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0
    # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤부터 흐른 시간 (초)
    index = 0 # 다음에 회전할 정보
    q = [(x, y)]

    while True:
        # 이동한 위치 계산
        nextX = x + dx[direction]
        nextY = y + dy[direction]

        # 이동한 위치가 맵 범위 안에 있고, 뱀의 몸통이 없는 위치일 때
        if 1 <= nextX <= n and 1 <= nextY <= n and data[nextX][nextY] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if data[nextX][nextY] == 0:
                # 뱀 머리 이동
                data[nextX][nextY] = 2
                q.append((nextX, nextY))
                # 꼬리 제거
                pastX, pastY = q.pop(0)
                data[pastX][pastY] = 0
            # 사과가 있다면 이동 후 꼬리 그대로 둠
            if data[nextX][nextY] == 1:
                data[nextX][nextY] = 2
                q.append((nextX, nextY))
        # 벽이나 몸통에 부딪혔다면
        else:
            time += 1
            break
        
        x, y = nextX, nextY # 뱀의 머리 위치 이동
        time += 1

        # 회전할 시간인 경우
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    
    return time

print(simulate())
