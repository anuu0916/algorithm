# 14889 스타트와 링크

n = int(input())
s = []
visited = [0 for _ in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    s.append(tmp)

def dfs(depth, begin):
    global min_value
    
    if depth == n/2:
        start = 0
        link = 0
        # print(visited)
        for j in range(n):
            for k in range(j+1, n):
                if visited[j] * visited[k] == 1:
                    start += s[j][k] + s[k][j]
                elif visited[j]+visited[k] == 0:
                    link += s[j][k] + s[k][j]

        # print(start, link)
        min_value = min(min_value, abs(start - link))
        return
    
    # print(begin)
    for i in range(begin, n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth+1, i+1)
            visited[i] = 0

min_value = int(1e9)
dfs(0, 0)
print(min_value)
