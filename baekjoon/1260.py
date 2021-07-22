# 1260 DFS와 BFS
import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(n)]
visited = [False for _ in range(n)]

for _ in range(m):
    src, dst = map(int, sys.stdin.readline().split())
    adj[src-1].append(dst)
    adj[src-1].sort()
    adj[dst-1].append(src)
    adj[dst-1].sort()


def dfs(vertex):
    visited[vertex-1] = True
    print(vertex, end=" ")
    for node in adj[vertex-1]:
        if visited[node-1] is False:
            dfs(node)


def bfs(vertex):
    queue = deque()
    queue.append(vertex)
    while len(queue) > 0:
        top = queue.popleft()
        if visited[top-1] is False:
            print(top, end=" ")
            visited[top - 1] = True
            queue.extend(adj[top - 1])


dfs(v)
print()
visited = [False for _ in range(n)]
bfs(v)
