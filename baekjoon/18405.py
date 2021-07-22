# 18405 경쟁적 전염
import sys
dir = [[1, 0], [-1, 0], [0, -1], [0, 1]]  # 상하좌우 계산 좌표
n, k = map(int, sys.stdin.readline().split())  # 입력
exam = list()  # 시험관

for i in range(n):
    exam.append(list(map(int, sys.stdin.readline().split())))  # 시험관 입력

s, x, y = map(int, sys.stdin.readline().split())


# 전염 계산 함수
def infect(v):
    virus = list()  # v번 바이러스 위치 저장할 배열
    # v번 바이러스 위치 찾음
    for j in range(n):
        if v in exam[j]:
            # 처음에 index 함수로 찾았는데 그러니까 한 개씩밖에 안 찾아져서 for문 돌렸습니다..
            for z in range(n):
                if exam[j][z] == v:
                    virus.append([j, z])

    # 바이러스 상하좌우 전염
    for (row, col) in virus:
        for d in dir:
            nextX = row + d[0]
            nextY = col + d[1]
            # 좌표 유효한지 검사
            if nextX > -1 and nextX < n and nextY > -1 and nextY < n and exam[nextX][nextY] == 0:
                exam[nextX][nextY] = v


# s번 (s초)동안 반복
for i in range(s):
    # 이미 x,y 좌표에 바이러스가 있으면 출력
    if exam[x-1][y-1] != 0:
        print(exam[x-1][y-1])
        exit()

    # 1번부터 k번까지 순서대로 전염
    for m in range(k):
        infect(m+1)

print(exam[x-1][y-1])
