# 18352 특정 거리의 도시 찾기
import sys
from collections import deque
INF = int(1e9)
n, m, k, x = map(int, sys.stdin.readline().split())

# 도시 연결 인접리스트
graph = [[] for _ in range(n + 1)]
# 방문 표시
visited = [False for _ in range(n + 1)]
# 최단거리 저장
distance = [INF for _ in range(n + 1)]

# 도시 연결 정보 입력
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(start):
    # 시작 도시, 거리 큐 삽입
    # 출발 도시 x에서 출발 도시 x로 가는 최단 거리는 0이므로 거리 0으로 삽입
    queue = deque([[start, 0]])
    visited[start] = True
    distance[start] = 0

    while queue:
        # 큐 pop
        v, w = queue.popleft()
        # 연결된 모든 도시에 대해
        for i in graph[v]:
            # 방문하지 않은 도시라면
            if not visited[i]:
                # 최단거리 갱신 (도로 가중치는 1)
                distance[i] = min(w + 1, distance[i])
                # 큐 삽입
                queue.append([i, distance[i]])
                visited[i] = True


bfs(x)

# 최단거리가 k인 도시가 있는지 검사
check = 0
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check += 1

# 최단거리 k인 도시가 없다면 -1 출력
if check == 0:
    print(-1)
