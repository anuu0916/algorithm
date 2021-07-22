# 2178 미로 탐색
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
maze = list()

for _ in range(n):
    tmp = list(sys.stdin.readline().rstrip())
    maze.append(tmp)

adj = {}
trace = {}


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
    for j in range(m):
        if maze[i][j] == "1":
            if j+1 < m and maze[i][j+1] == "1":
                insert(i, j, i, j+1)

            if i+1 < n and maze[i+1][j] == "1":
                insert(i, j, i+1, j)


queue = deque()
queue.append((0, 0))
visited = list()
trace[(0, 0)] = 1

# 최단경로에서 막힘.....
# 처음에는 그래프 depth를 찾으면 되겠다고 생각했는데 depth는 트리에만 있음
# 그래서 큐에 자식노드 추가하는 횟수를 카운트했다가 안됨. 당연함...
# 결국 구글링해서 지금까지 거쳐온 최단 노드의 수를 세는 식으로 했습니다.
while len(queue) > 0:
    top = queue.popleft()

    if top == (n-1, m-1):
        break

    if top not in visited:
        visited.append(top)
        for next in adj[top]:
            if next not in trace.keys():
                trace[next] = trace[top] + 1
        queue.extend(adj[top])


print(trace[(n-1, m-1)])
