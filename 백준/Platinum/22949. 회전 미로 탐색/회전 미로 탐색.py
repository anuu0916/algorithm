# 22949 회전 미로 탐색
# 이 문제에서 좌표는 배열[y, x]로 표현
from collections import deque
k = int(input())
n = 4*k
origin = []
cur = []

# 상하좌우 이동 + 가만히 있는 거 포함
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

for i in range(n):
    tmp = list(input())
    if len(cur) == 0:
        for j in range(n):
            if tmp[j] == 'S':
                cur = [i, j]
    origin.append(tmp)


# 구역번호 구하는 함수. 미로 범위를 벗어나면 -1 리턴
def get_division(y, x):
    if 0 <= y < n and 0 <= x < n:
        return y//4+x//4
    else:
        return -1


def get_rotated(y, x):
    # 4의 배수만큼을 빼둠
    baseY = (y//4) * 4
    baseX = (x//4) * 4
    # 4x4 구역으로 치환하고 회전
    y %= 4
    x %= 4
    # (y, x)를 시계방향 90도 회전하면 (x, n-1-y)
    # 회전시킨 뒤 빼뒀던 base 값들을 더함
    return [baseY+x, baseX+3-y]


def rotate_arr(array, div):
    sy = (div // k) * 4
    sx = (div % k) * 4

    tmp = [row[sx:sx+4] for row in array[sy:sy+4]]
    rotated = []
    for each in zip(*tmp[::-1]):
        rotated.append(list(each))

    for i in range(4):
        for j in range(4):
            array[sy+i][sx+j] = rotated[i][j]

    return array


arr = []
arr2 = [item[:] for item in origin]
arr.append(arr2)
for i in range(3):
    arr2 = [item[:] for item in arr2]
    for j in range(k**2):
        arr2 = rotate_arr(arr2, j)
    arr.append(arr2)


# y, x, 회전각도, 시간
# 회전각도 0 : 0도, 1 : 90도, 2 : 180도, 3 : 270도
queue = deque([[cur[0], cur[1], 0, 0]])
result = -1

# 4가지 각도 방향에 따라 방문 체크 다르게 해줌
visited = [[[0] * n for _ in range(n)] for _ in range(4)]
visited[0][cur[0]][cur[1]] = 1


def print_arr(arr, d, y, x):
    for i in range(n):
        for j in range(n):
            if i == y and j == x:
                print("*", end=" ")
            else:
                print(arr[d][i][j], end=" ")
        print()


while queue:
    y, x, d, time = queue.popleft()
    # print("--------%d---------" % time)
    # print_arr(arr, d, y, x)
    cdiv = get_division(y, x)  # 현재 구역번호

    if arr[d][y][x] == 'E':
        result = time
        break

    for i in range(5):
        ny = y + dy[i]
        nx = x + dx[i]
        ndiv = get_division(ny, nx)
        if ndiv == -1:
            continue
        nd = 0
        if ndiv == cdiv:
            nd = (d+1) % 4
        else:
            nd = 1

        [ny, nx] = get_rotated(ny, nx)
        if visited[nd][ny][nx] == 0 and arr[nd][ny][nx] != '#':
            visited[nd][ny][nx] = 1
            queue.append([ny, nx, nd, time+1])

print(result)
