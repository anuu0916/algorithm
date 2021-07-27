# 2606 바이러스
import sys
from collections import deque
n = int(input())
k = int(input())
adj = {}

for i in range(k):
    a, b = map(int, sys.stdin.readline().split())

    if a not in adj:
        adj[a] = [b]
    else:
        adj[a].append(b)

    if b not in adj:
        adj[b] = [a]
    else:
        adj[b].append(a)

visited = [0 for _ in range(n+1)]
stack = deque()
stack.append(1)
visited[1] = 1
cnt = 0

while stack:
    top = stack.pop()

    for i in adj[top]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = 1
            stack.append(i)

print(cnt)
