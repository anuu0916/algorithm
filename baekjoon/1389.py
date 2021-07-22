# 1389 케빈 베이컨의 6단계 법칙
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
adj = {}

# 입력받은 관계만큼 인접리스트 생성
# 관계 중복으로 입력될 수도 있다고 해서 처음엔 집합으로 하려고 했다가,
# 집합은 인덱싱이 안돼고 일일이 list 변환하는것도 귀찮아서
# 그냥 방문 체크하는거에서 걸러지지 않을까 해서 입력받는대로 다 넣음
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    if a not in adj:
        adj[a] = [b]
    else:
        adj[a].append(b)

    if b not in adj:
        adj[b] = [a]
    else:
        adj[b].append(a)

# 케빈 베이컨 수를 저장할 배열
# i번 사람의 케빈 베이컨 수를 i-1번 인덱스에 저장
kevin = [0 for _ in range(n)]

# 모든 사람의 케빈 베이컨 수를 다 구해야 하므로 n번 반복
for i in range(n):
    visited = [0 for _ in range(n)]
    queue = deque()
    queue.append((i+1, 0))  # 먼저 자기 자신을 큐에 넣음
    bacon = 0  # 케빈 베이컨 수 누적할 변수

    while queue:
        top = queue.popleft()

        if visited[top[0]-1] == 0:
            visited[top[0]-1] = 1
            bacon += top[1]  # 최단거리 (케빈 베이컨) 누적
            for node in adj[top[0]]:
                queue.append((node, top[1]+1))

    kevin[i] = bacon  # 배열에 저장

# 최솟값을 가지고 있는 배열의 인덱스 구함
# index 내장함수를 쓰면 가장 작은 인덱스값이 나옴!!
print(kevin.index(min(kevin))+1)
