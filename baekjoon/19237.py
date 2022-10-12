# 19237 어른 상어
import copy
n, m, k = map(int, input().split())
# 위, 아래, 왼쪽, 오른쪽
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

shark = [[] * 2 for _ in range(m+1)]  # 상어 좌표
scent = []  # 냄새 상태 맵
shark_dir = [0]
shark_num = m

for i in range(n):
    stmp = list(map(int, input().split()))
    tmp = [[]*2 for _ in range(n)]
    for j in range(n):
        if stmp[j] > 0:
            shark[stmp[j]] = [i, j]
            tmp[j] = [stmp[j], k]
        else:
            tmp[j] = [0, 0]
    scent.append(tmp)

shark_dir.extend(list(map(int, input().split())))

prior = [[]]
for i in range(m):
    tmp = []
    for j in range(4):
        tmp.append(list(map(int, input().split())))
    prior.append(tmp)


def print_arr():
    global result
    print("---------%d---------" % result)
    for i in range(n):
        print(scent[i])
    print(shark)


# 냄새가 4인 곳이 현재 상어가 있는 위치
result = 0
while result < 1001:
    # print_arr()
    if shark_num <= 1:
        break
    result += 1

    # 이전 상태
    before = copy.deepcopy(scent)
    # 상어 이동하고 냄새 뿌리기
    for s in range(1, m+1):
        if shark[s] == [-1, -1]:
            continue

        sx = shark[s][0]
        sy = shark[s][1]
        sdir = shark_dir[s]
        next_prior = [-1, -1, -1]
        for i in range(4):
            ndir = prior[s][sdir-1][i]
            nx = sx + dx[ndir]
            ny = sy + dy[ndir]
            if 0 <= nx < n and 0 <= ny < n:
                if before[nx][ny][1] == 0:
                    next_prior = [nx, ny, ndir]
                    break
                elif before[nx][ny][0] == s and next_prior[2] == -1:
                    next_prior = [nx, ny, ndir]

        nx, ny, ndir = next_prior[0], next_prior[1], next_prior[2]
        if scent[nx][ny][1] == k+1:  # 같은 칸에 있을 경우
            # 상어 번호대로 반복하니 뒤에 들어온 상어(현재 상어)가 방출
            shark[s] = [-1, -1]
            shark_num -= 1
            shark_dir[s] = 0
        else:
            shark[s] = [nx, ny]
            scent[nx][ny] = [s, k+1]
            shark_dir[s] = ndir

    # 냄새 희석
    for i in range(n):
        for j in range(n):
            if scent[i][j][1] == 1:
                scent[i][j] = [0, 0]
            elif scent[i][j][1] > 1:
                scent[i][j][1] -= 1

if result <= 1000:
    print(result)
else:
    print(-1)
