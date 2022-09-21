# 92343 양과 늑대
from collections import deque

def solution(info, edges):
    n = len(info)
    answer = 0
    # 인접리스트
    adj = [[] for _ in range(n + 1)]
    # 방문
    visited = [False for _ in range(n + 1)]
    
    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])
    
    # for i in range(n):
    #     print(i, adj[i])
    # print("------------------")
    queue = deque([0])
    balance = 0

    top = 0
    node = adj[top][0]
    adj[node].extend(adj[top])
    
    # for i in range(n):
    #     print(i, adj[i])
    # print("------------------")

    while queue:
        top = queue.pop()
        print(top)
        info[top] = 2  # 방문 표시

        if info[top] == 0:
            balance += 1
        elif info[top] == 1:
            balance -= 1
        
        answer = max(answer, balance)

        for node in adj[top]:
            if info[node] == 0:
                adj[node].extend(adj[top])
                queue.append(node)
            elif info[node] == 1 and balance > 1:
                adj[node].extend(adj[top])
                queue.append(node)
    
    return answer


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))