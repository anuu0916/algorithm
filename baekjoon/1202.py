# 1202 보석 도둑
import sys
import heapq
n, k = map(int, sys.stdin.readline().split())
bag = []
jewel = []

for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewel, [w, v])

for i in range(k):
    heapq.heappush(bag, int(input()))

result = 0
tmp = []  # 현재 가방에 담을 수 있는 무게의 보석들

for i in range(k):
    capacity = heapq.heappop(bag)

    # 현재 가방에 담을 수 있는 무게 이하인 모든 보석에 대해
    while jewel and capacity >= jewel[0][0]:
        [w, v] = heapq.heappop(jewel)
        # 보석의 가치를 힙에 넣어줌
        # 파이썬에서 heapq는 최소힙만을 지원하기 때문에, 최대힙을 만들려면 -를 붙여서 푸시
        heapq.heappush(tmp, -v)

    if tmp:
        result -= heapq.heappop(tmp)

print(result)
