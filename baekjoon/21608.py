# 21608 상어 초등학교
n = int(input())
sn = n**2
like = [0] * (sn+1)  # i번의 학생이 좋아하는 학생 list
seat = [[0] * n for _ in range(n)]  # 교실 자리
order = [0] * sn  # 학생 순서
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(sn):
    tmp = list(map(int, input().split()))
    order[i] = tmp[0]
    like[tmp[0]] = tmp[1:]

# 첫 번째 학생은 무조건 (1, 1) 자리 배정
# seat[1][1] = order[0]

for o in range(sn):
    num = order[o]
    # print("----------%d---------" % num)
    prior = [-1, -1]  # 가장 만족도가 높은 자리 좌표
    max_sati = 0  # 최대 만족도 갱신
    # 만족도 계산 : 좋아하는 학생 인접한 수 * 10, 비어있는 칸 수 * 1,
    # 좌표 (r, c)라면 (n-r) * 100, (n-c) * 1
    # n 범위가 20이라 위에처럼은 못하네...
    max_pos_sati = 0  # 좌표 우선순위 계산

    for i in range(n):
        for j in range(n):
            if seat[i][j] == 0:
                x = i
                y = j
                pos_sati = (n - x) * 100 + (n - y)
                sati = 0
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if seat[nx][ny] == 0:
                            sati += 1
                        elif seat[nx][ny] in like[num]:
                            sati += 10
                # print("(%d, %d) sati : %d, pos_sati : %d" % (i, j, sati, pos_sati))
                if sati > max_sati:
                    max_sati = sati
                    max_pos_sati = pos_sati
                    prior = [x, y]
                elif sati == max_sati and pos_sati > max_pos_sati:
                    # print("max_pos_sati", max_pos_sati)
                    max_pos_sati = pos_sati
                    prior = [x, y]

    # print("final", prior)
    seat[prior[0]][prior[1]] = num

# for i in range(n):
#     print(seat[i])

result = 0
for i in range(n):
    for j in range(n):
        num = seat[i][j]
        cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if seat[nx][ny] in like[num]:
                    cnt += 1
        if cnt > 0:
            result += 10 ** (cnt - 1)

print(result)
