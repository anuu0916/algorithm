# 1715 카드 정렬하기 (두 번째 풀이)
import heapq
n = int(input())
card = []

for i in range(n):
    card.append(int(input()))

result = 0
heapq.heapify(card)

while len(card) > 1:
    # 가장 작은 값 2개 pop
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)

    # 비교 횟수 (두 값을 더한 값) 누적
    result += n1+n2

    # 카드 더미 다시 push
    heapq.heappush(card, n1+n2)

print(result)