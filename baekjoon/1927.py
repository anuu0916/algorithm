# 1927 최소 힙
import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
heapq.heapify(heap)

for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
