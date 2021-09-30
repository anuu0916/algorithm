# 9372 상근이의 여행
import sys
t = int(input())


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


for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    parent = [0] * (n + 1)
    result = 0

    # 부모 테이블에서 부모를 자기 자신으로 초기화
    for j in range(1, n + 1):
        parent[j] = j

    # 간선 정보 입력
    for j in range(m):
        a, b = map(int, sys.stdin.readline().split())
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += 1

    print(result)
