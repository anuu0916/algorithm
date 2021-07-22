from collections import deque

res = [0] * 100003

n, k = map(int, input().split())

queue = deque()
queue.append(n)

while queue :
    x = queue.popLeft()
    if x == k :
        print(res[x])
        break
    for nx in (x - 1, x+1, x*2) :
        if 0 <= nx <= 100003 and not res[nx] :
            res[nx] = res[x] + 1
            queue.append(nx)