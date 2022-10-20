# 22942 데이터 체커
import sys
from collections import deque
n = int(input())
circles = []


class Circle:
    def __init__(self, p, isOpen, num):
        self.p = p
        self.isOpen = isOpen
        self.num = num


for i in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles.append(Circle(x - r, True, i))  # 여는 괄호
    circles.append(Circle(x + r, False, i))  # 닫는 괄호

circles.sort(key=lambda x: x.p)
stack = deque([])
result = "YES"

for i in range(2*n):
    nxt = circles[i]
    cur = stack[-1] if stack else nxt
    if cur.num == nxt.num and cur.isOpen and not cur.isOpen:
        stack.pop()
    else:
        if cur.num != nxt.num and cur.isOpen and not nxt.isOpen:
            result = "NO"
            break
        stack.append(nxt)

print(result)
