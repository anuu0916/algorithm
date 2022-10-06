# 15685 드래곤 커브
n = int(input())
arr = []
# 크기 100x100인 격자
board = [[0] * 101 for _ in range(101)]
# 좌표는 (y,x) 순서
# 드래곤 커브 방향
# 동 북 서 남
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)


for i in range(n):
    x, y, d, g = arr[i][0], arr[i][1], arr[i][2], arr[i][3]

    move = [d]
    for j in range(g):
        for m in range(len(move)-1, -1, -1):
            move.append((move[m]+1)%4)
    
    board[y][x] = 1

    for m in move:
        x += dx[m]
        y += dy[m]
        if 0 <= x <= 100 and 0 <= y <= 100:
            board[y][x] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if (board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]) == 4:
            cnt += 1

print(cnt)
