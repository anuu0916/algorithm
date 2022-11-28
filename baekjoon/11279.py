# 11279 최대 힙
import heapq
import sys
input = sys.stdin.readline
n = int(input())
heap = []
heapq.heapify(heap)

for i in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            large = heapq.heappop(heap)
            print(-large)
    else:
        heapq.heappush(heap, -num)
