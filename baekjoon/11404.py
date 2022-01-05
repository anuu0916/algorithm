# 11404 플로이드
import sys
import heapq
INF = int(1e9)
n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수
graph = [[] for _ in range(n + 1)]

# 버스 정보 입력
for i in range(m):
    # 시작 도시 a, 도착 도시 b, 한 번 타는 데 필요한 비용 c
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])


def dijkstra(start):
    distance = [INF] * (n + 1)  # 초기화
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드 pop
        dist, now = heapq.heappop(q)
        # 이미 처리한 노드라면 무시
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + node[1]
            if cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(q, [cost, node[0]])

    for j in range(1, n + 1):
        if distance[j] == INF:
            print(0, end=" ")
        else:
            print(distance[j], end=" ")
    print()


for i in range(1, n + 1):
    dijkstra(i)
