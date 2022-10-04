# 14500 테트로미노
# 구글링 코드 참고

import sys
n, m = map(int, sys.stdin.readline().split())
arr = []
visited = [[0] * m for _ in range(n)]
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))


def dfs(depth, x, y, value):
    global max_value

    if depth == 4:
        max_value = max(max_value, value)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(depth+1, nx, ny, value + arr[nx][ny])
            visited[nx][ny] = 0


# ㅗ, ㅜ, ㅓ, ㅏ 모양
def dfs2(x, y):
    global max_value
    for i in range(4):
        value = arr[x][y]
        # 한 방향을 제외하고 확장하기
        for j in range(3):
            t = (i+j)%4
            nx = x + dx[t]
            ny = y + dy[t]

            if 0 <= nx < n and 0 <= ny < m:
                value += arr[nx][ny]
            else:
                break
        
        max_value = max(max_value, value)


max_value = 0

for a in range(n):
    for b in range(m):
        visited[a][b] = 1
        dfs(1, a, b, arr[a][b])
        visited[a][b] = 0

        dfs2(a, b)

print(max_value)

