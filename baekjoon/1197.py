# 1197 최소 스패닝 트리
import sys
n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)
edges = []

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 간선 정보 입력
for i in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((cost, a, b))

edges.sort()  # 비용순으로 정렬
last = 0  # 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선
result = 0  # 최소 비용


# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result)
