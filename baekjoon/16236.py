# 16236 아기 상어
from collections import deque
n = int(input())
arr = []
shark = []
fish = []
grow = 2
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(n):
        if 0 < tmp[j] < 7:
            fish.append([tmp[j], i, j])
        elif tmp[j] == 9:
            shark = [i, j]

fish.sort()
fish = deque(fish)

if len(fish) == 0 or fish[0][0] > 1:
    print("0")
    exit()


def shortest():
    queue = deque([[shark[0], shark[1], 0]])
    visited = [[0] * n for _ in range(n)]
    visited[shark[0]][shark[1]] = 1
    edible = []
    while queue:
        # print(queue)
        x, y, dis = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] <= grow and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append([nx, ny, dis+1])
                    if 0 < arr[nx][ny] < grow:
                        # print("edible %d %d %d" % (nx, ny, dis+1))
                        edible.append([nx, ny, dis+1])

    return sorted(edible, key=lambda x: (x[2], x[0], x[1]))


cnt = 0
result = 0
while True:
    eat = shortest()

    if len(eat) == 0:
        break

    nx, ny, dis = eat[0][0], eat[0][1], eat[0][2]
    result += dis
    arr[shark[0]][shark[1]], arr[nx][ny] = 0, 0
    shark = [nx, ny]
    cnt += 1

    if cnt == grow:
        cnt = 0
        grow += 1

print(result)
