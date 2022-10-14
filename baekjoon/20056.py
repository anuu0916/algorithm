# 20056 마법사 상어 파이어볼
from collections import deque
N, M, K = map(int, input().split())
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 파이어볼의 정보
# 좌표 r, c, 질량 m, 방향 d, 속력 s
queue = []
arr = [[deque([]) for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    queue.append([r-1, c-1, m, s, d])


def print_arr():
    print("--------------------")
    for i in range(N):
        print(arr[i])
    print(queue)


queue = deque(queue)
for cnt in range(K):
    while queue:
        r, c, m, s, d = queue.popleft()
        nr = (r + (dr[d] * s)) % N
        nc = (c + (dc[d] * s)) % N
        arr[nr][nc].append([m, s, d])
    # print_arr()
    for i in range(N):
        for j in range(N):
            cnt = len(arr[i][j])
            if cnt > 1:
                sum_m, sum_s, cnt_odd, cnt_even = 0, 0, 0, 0
                while arr[i][j]:
                    m, s, d = arr[i][j].popleft()
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

                if sum_m // 5 > 0:
                    if cnt_even == 0 or cnt_odd == 0:
                        for d in range(0, 8, 2):
                            queue.append([i, j, sum_m//5, sum_s//cnt, d])
                    else:
                        for d in range(1, 8, 2):
                            queue.append([i, j, sum_m//5, sum_s//cnt, d])

            if cnt == 1:
                m, s, d = arr[i][j].popleft()
                queue.append([i, j, m, s, d])

result = 0
for fire in queue:
    result += fire[2]

print(result)
