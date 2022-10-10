# 17144 미세먼지 안녕!
r, c, t = map(int, input().split())
arr = []
up = -1
down = -1

for i in range(r):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    if tmp[0] == -1 and up == -1:
        up = i
        down = i+1

# 미세먼지 확산
def spread():
    # 상하좌우 순서 상관 X
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                tmp = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                        tmp_arr[nx][ny] += arr[i][j] // 5
                        tmp += arr[i][j] // 5
                arr[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp_arr[i][j]


# 공기청정기 위쪽 순환
def move_up():
    # 우상좌하 순서
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    dir = 0
    # 전 칸의 미세먼지의 양.
    # 공기청정기에서 나오는 바람은 미세먼지 양이 0이므로 before를 0으로 설정
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == up and y == 0:
            break
        if 0 <= nx < r and 0 <= ny < c:
            # swap
            arr[x][y], before = before, arr[x][y]
            x = nx
            y = ny
        else:
            dir += 1


# 공기청정기 아래쪽 순환
def move_down():
    # 우하좌상 순서
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    # 전 칸의 미세먼지의 양.
    # 공기청정기에서 나오는 바람은 미세먼지 양이 0이므로 before를 0으로 설정
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == down and y == 0:
            break
        if 0 <= nx < r and 0 <= ny < c:
            # swap
            arr[x][y], before = before, arr[x][y]
            x = nx
            y = ny
        else:
            dir += 1


def print_arr(time):
    print("----------------%d----------------" % time)
    for i in range(r):
        print(arr[i])


for time in range(t):
    spread()
    move_up()
    move_down()
    # print_arr(time)

result = 0
for i in range(r):
    result += sum(arr[i])

print(result+2)
