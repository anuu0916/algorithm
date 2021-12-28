# 1753 최단경로
import sys
import heapq
INF = int(1e9)  # 무한을 의미하는 변수

# 정점의 개수 v와 간선의 개수 e 입력
V, E = map(int, sys.stdin.readline().split())
# 시작 정점의 번호 입력
start = int(input())
# 연결리스트
graph = [[] for i in range(V + 1)]
# 최단 거리 테이블
distance = [INF] * (V + 1)

# 연결 정보 입력
for i in range(E):
    # u에서 v로 가는 가중치 w인 간선이 존재
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])


def dijkstra(s):
    q = []
    # (가중치, 정점) 큐에 삽입
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        # 이미 방문한 노드일 경우 continue
        if distance[now] < dist:
            continue
        # 현재 노드의 인접 정점 확인
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
