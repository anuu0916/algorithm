# 1021 회전하는 큐
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque(list(range(1, n+1)))
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    while True:
        if queue[0] == num:
            queue.popleft()
            break
        else:
            if queue.index(num) <= len(queue)//2:
                while queue[0] != num:
                    queue.rotate(-1)
                    cnt += 1
            else:
                while queue[0] != num:
                    queue.rotate(1)
                    cnt += 1

print(cnt)
