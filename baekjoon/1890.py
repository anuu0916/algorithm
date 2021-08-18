# 1890 점프
import sys
n = int(input())
board = list()
d = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

d[0][0] = 1  # 왼쪽 위 칸 방문

for i in range(n):
    for j in range(n):
        if d[i][j] > 0:
            if i == n-1 and j == n-1:  # 맨 오른쪽 아래칸일 경우 끝냄
                break

            now = board[i][j]

            if j + now < n:
                d[i][j + now] += d[i][j]
            if i + now < n:
                d[i + now][j] += d[i][j]

print(d[n-1][n-1])
