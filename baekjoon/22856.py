# 22856 트리 순회
import sys
from collections import deque
n = int(input())
visited = [0] * (n+1)

class Node:
    def __init__(self, no, left, right):
        self.no = no
        self.left = left
        self.right = right


tree = {}
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a] = Node(a, b, c)

# 간선을 2번 방문하지 않는 경우는 가장 오른쪽 노드들을 방문할 때가 유일함
cnt = 0
right = tree[1].right
while right != -1:
    cnt += 1
    right = tree[right].right

print((n-1)*2 - cnt)
