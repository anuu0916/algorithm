# 2583 영역 구하기
import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())
# 사각형을 그릴 모눈종이 그래프. 1로 채움
graph = [[1 for _ in range(n)] for _ in range(m)]

# 사각형을 그린 곳은 0으로 초기화
for i in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for y in range(y2-1, y1-1, -1):
        for x in range(x2-1, x1-1, -1):
            graph[y][x] = 0

# 이 이후로는 단지번호구하기와 똑같이 구했습니다...
adj = {}  # 인접리스트
cnt = 0  # 1 개수 카운트


# 인접리스트 만드는 함수.
# (x, y)와 (nextX, nextY)가 인접할 때 딕셔너리에 넣어줌
def insert(x, y, nextX, nextY):
    if (x, y) not in adj.keys():
        adj[(x, y)] = [(nextX, nextY)]
    else:
        adj[(x, y)].append((nextX, nextY))

    if (nextX, nextY) not in adj.keys():
        adj[(nextX, nextY)] = [(x, y)]
    else:
        adj[(nextX, nextY)].append((x, y))


for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            cnt += 1
            insert(i, j, i, j)  # 한 칸만 있는 영역도 카운트하기 위해 자기자신도 인접리스트에 넣음
            if j+1 < n and graph[i][j+1] == 1:  # 오른쪽 칸과 인접한지
                insert(i, j, i, j+1)

            if i+1 < m and graph[i+1][j] == 1:  # 아래 칸과 인접한지
                insert(i, j, i+1, j)


visited = [[0 for _ in range(n)] for _ in range(m)]
check = 0  # 방문한 노드 개수 카운트
# 영역의 넓이를 넣을 배열 ex) [1, 7, 13]이면 영역이 3개, 넓이가 각각 1, 7, 13
areas = list()

# 영역을 다 돌 때까지
while check < cnt:
    queue = deque()
    area = 0  # 집의 개수 카운트

    # 방문하지 않은 칸 하나 정해서 큐에 넣음
    # 여기서 node : (x, y), node[0] : x, node[1] : y
    for node in adj.keys():
        if visited[node[0]][node[1]] == 0:
            queue.append(node)
            break

    # 위에서 넣은 노드(칸)을 시작으로 bfs
    while len(queue) > 0:
        top = queue.popleft()
        # print(top)

        if visited[top[0]][top[1]] == 0:
            check += 1  # 전체 방문한 칸의 개수 증가
            area += 1  # 영역 안에서 방문한 칸의 개수 증가
            visited[top[0]][top[1]] = 1
            queue.extend(adj[top])

    # 해당 영역의 칸 개수 (넓이) append
    areas.append(area)

# areas 배열의 길이 = 영역의 개수
print(len(areas))
areas.sort()  # 오름차순으로 정렬하고 출력함
for i in areas:
    print(i, end=" ")

