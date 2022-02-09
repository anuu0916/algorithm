# 16234 인구 이동
import sys
from collections import deque
n, l, r = map(int, sys.stdin.readline().split())
a = []
union = []
# 상하좌우 이동
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, y, u, visited):
    stack = deque([[x, y]])
    visited[x][y] = True

    # dfs
    while stack:
        x, y = stack.pop()

        # 상하좌우 이동
        for _ in range(4):
            nextY = y + dy[_]
            nextX = x + dx[_]

            # 인덱스가 배열 범위 내인지, 방문하지 않은 국가인지 검사
            if 0 <= nextY < n and 0 <= nextX < n and not visited[nextX][nextY]:
                # 인구 수 차이가 l이상 r이하일 때
                if l <= abs(a[x][y] - a[nextX][nextY]) <= r:
                    # 연합에 추가
                    union[u].append((nextX, nextY))
                    visited[nextX][nextY] = True
                    stack.append([nextX, nextY])


# 연합 안의 국가 간 인구 이동
def move_people(u):
    sum = 0
    num = len(u)
    for x, y in u:
        sum += a[x][y]
    for x, y in u:
        a[x][y] = sum // num


# 인구 이동에 걸리는 날짜
result = 0

while True:
    union = []  # 연합 국가 인덱스를 저장할 배열
    uni = 0  # 연합의 개수 index
    visited = [[False for _ in range(n)] for _ in range(n)]

    # 방문하지 않은 국가일 때 dfs 진행
    for i in range(n):
       for j in range(n):
            if not visited[i][j]:
                # 기본적으로 연합에 국가 하나씩은 들어있게 설정
                union.append([(i, j)])
                dfs(i, j, uni, visited)
                uni += 1
    
    # 연합인 국가끼리 인구 이동 수행
    for u in union:
        # 연합 안에 있는 국가가 1개일 때는 인구이동 하지 않음
        if len(u) > 1:
            move_people(u)

    # 연합의 개수가 n*n개일 때
    # 즉, 모든 국가에서 연합이 이루어지지 않았을 때 break
    if len(union) >= n*n:
        break
    else:
        result += 1


print(result)
