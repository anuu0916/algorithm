# 14499 주사위 굴리기
import sys
n, m, x, y, k = map(int, sys.stdin.readline().split())
arr = []
dice = [0, 0, 0, 0, 0, 0]
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split()))) 

move = list(map(int, sys.stdin.readline().split()))

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1:  # 동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2:  # 서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3:  # 북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    elif dir == 4:  # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


for i in range(k):
    nextX = x + dx[move[i]-1]
    nextY = y + dy[move[i]-1]

    # print("--------", i, "--------")
    # print("현재 : ", x, y)
    # print("이동 : ", nextX, nextY)

    if 0 <= nextX < n and 0 <= nextY < m:
        turn(move[i])
        x = nextX
        y = nextY

        if arr[nextX][nextY] == 0:
            arr[nextX][nextY] = dice[5]
        else:
            dice[5] = arr[nextX][nextY]
            arr[nextX][nextY] = 0
        
        # print("주사위 이동 후", dice)
        print(dice[0])
        
