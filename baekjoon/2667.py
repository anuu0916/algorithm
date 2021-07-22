# 2667 단지번호붙이기
import sys
from collections import deque
n = int(input())  # 지도의 크기
apart = list()  # 단지 배열
adj = {}  # 인접리스트
cnt = 0  # 1 개수 (집 개수) 카운트 변수

# 단지 배열 입력받음
for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip())  # 문자열을 배열로 변환해서 넣어줌
    tmp = list(map(int, tmp))  # int로 변환
    # 단지 순회 확인을 위해 1 개수 카운트
    cnt += tmp.count(1)
    apart.append(tmp)


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


for i in range(n):
    for j in range(n):
        if apart[i][j] == 1:
            insert(i, j, i, j)  # 집 하나만 있는 단지도 카운트하기 위해 자기자신도 인접리스트에 넣음
            if j+1 < n and apart[i][j+1] == 1:  # 오른쪽 집과 인접한지
                insert(i, j, i, j+1)

            if i+1 < n and apart[i+1][j] == 1:  # 아래 집과 인접한지
                insert(i, j, i+1, j)


visited = [[0 for _ in range(n)] for _ in range(n)]
check = 0  # 방문한 노드(집) 개수 카운트
# 단지마다 집의 개수를 넣을 배열 ex) [7, 8, 9]면 단지가 3개, 집 개수가 각각 7,8,9
graph = list()

# 집을 다 돌 때까지
while check < cnt:
    queue = deque()
    house = 0  # 집의 개수 카운트

    # 방문하지 않은 집 하나 정해서 큐에 넣음
    # 여기서 node : (x, y), node[0] : x, node[1] : y
    for node in adj.keys():
        if visited[node[0]][node[1]] == 0:
            queue.append(node)
            break

    # 위에서 넣은 노드(집)을 시작으로 bfs
    while len(queue) > 0:
        top = queue.popleft()
        # print(top)

        if visited[top[0]][top[1]] == 0:
            check += 1  # 전체 방문한 집의 개수 증가
            house += 1  # 단지 안에서 방문한 집의 개수 증가
            visited[top[0]][top[1]] = 1
            queue.extend(adj[top])

    # 해당 단지의 집 개수 append
    graph.append(house)

# graph 배열의 길이 = 단지의 개수
print(len(graph))
graph.sort()  # 오름차순으로 정렬하고 출력함
for i in graph:
    print(i)
