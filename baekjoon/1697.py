# 1697 숨바꼭질
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())

queue = deque()
queue.append([n, 0])  # 현재위치, 최단거리 큐에 넣음
# 방문 배열 십만개짜리 만들기 무서워서 집합으로 선언함
# 집합이 in 연산 평균이 O(1)이라고 하네요 (리스트는 O(n))
visited = set()
visited.add(n)  # n에서부터 출발

while queue:
    top, step = queue.popleft()
    if top == k:  # k에 도착했으면 멈춤
        print(step)
        break

    if 0 <= top - 1 <= 100000 and top - 1 not in visited:
        visited.add(top - 1)
        queue.append([top - 1, step + 1])
    if 0 <= top + 1 <= 100000 and top + 1 not in visited:
        visited.add(top + 1)
        queue.append([top + 1, step + 1])
    if 0 <= top * 2 <= 100000 and top * 2 not in visited:
        visited.add(top * 2)
        queue.append([top * 2, step+1])
