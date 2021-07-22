# 2644 촌수계산
import sys
from collections import deque
n = int(input())
x, y = map(int, sys.stdin.readline().split())
m = int(input())
adj = [[] for _ in range(n)]
visited = [0 for _ in range(n)]

for _ in range(m):
    p, c = map(int, sys.stdin.readline().split())
    adj[p-1].append(c-1)
    adj[c-1].append(p-1)

queue = deque()
queue.append([x-1, 0])


while len(queue) > 0:
    top = queue.popleft()
    if top[0] == y-1:
        print(top[1])
        exit()

    if visited[top[0]] == 0:
        visited[top[0]] = 1
        for next in adj[top[0]]:
            queue.append([next, top[1] + 1])

print("-1")
