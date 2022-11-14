# 1655 가운데를 말해요
# 참고 : https://art-coding3.tistory.com/44
import heapq
import sys
n = int(sys.stdin.readline())
left = []
right = []
result = []

for i in range(n):
    num = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))
    
    if right and left[0][1] > right[0][0]:
        l = heapq.heappop(left)[1]
        r = heapq.heappop(right)[0]
        heapq.heappush(left, (-r, r))
        heapq.heappush(right, (l, l))
    
    result.append(left[0][1])

for res in result:
    print(res)
