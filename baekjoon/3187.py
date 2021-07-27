# 3187 양치기 꿍
import sys
from collections import deque
r, c = map(int, sys.stdin.readline().split())
fence = list()  # 입력을 저장할 배열
animal = list()  # 양 또는 늑대가 위치한 인덱스 저장할 배열
cnt = 0  # 양 또는 늑대의 수 총합

for i in range(r):
    fence.append(list(sys.stdin.readline().rstrip()))
    for j in range(c):
        if fence[i][j] == 'v' or fence[i][j] == 'k':
            cnt += 1  # 양 또는 늑대가 있을 때 cnt + 1
            animal.append((i, j))  # 인덱스 저장

visited = [[0 for _ in range(c)] for _ in range(r)]  # 방문 배열
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]
stack = deque()  # 재귀함수 제한 푸는거 귀찮아서 스택으로 구현했습니다
check = 0  # 방문한 양 또는 늑대의 위치 총합
sheep = 0  # 남은 양의 수
wolf = 0  # 남은 늑대의 수

while check < cnt:  # 모든 동물 칸을 방문할 때까지
    s = 0  # 현재 울타리 안의 양의 수
    w = 0  # 현재 울타리 안의 늑대의 수

    # 방문 안한 동물이 있으면 스택에 넣음
    for node in animal:
        if visited[node[0]][node[1]] == 0:
            stack.append(node)
            visited[node[0]][node[1]] = 1
            break

    # 울타리 안을 다 돌 때까지
    while stack:
        y, x = stack.pop()
        if fence[y][x] == 'v':  # 현재 위치에 양이 있을 경우
            w += 1
            check += 1
        elif fence[y][x] == 'k':  # 현재 위치에 늑대가 있을 경우
            s += 1
            check += 1

        # 상하좌우 탐색
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            # 조건문 길게 쓰기 싫어서 나눠서 썼습니다...
            if 0 <= nextX < c and 0 <= nextY < r:
                if fence[nextY][nextX] != '#' and visited[nextY][nextX] == 0:
                    visited[nextY][nextX] = 1
                    stack.append([nextY, nextX])

    if s > w:
        sheep += s
    else:
        wolf += w

print(sheep, wolf)
