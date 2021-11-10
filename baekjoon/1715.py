# 1715 카드 정렬하기
# 구글링했습니다..
# 최솟값, 최대값을 계속해서 호출할 때 우선순위 큐 (heap Queue) 사용
# heapq는 데이터 추가, 삭제시마다 자동으로 최소 힙을 만들어준다
import heapq
n = int(input())
card = []

for i in range(n):
    card.append(int(input()))

result = 0
heapq.heapify(card)
# n = 1일 경우에는 비교가 필요없음
while len(card) > 1:
    # 최솟값 두 개를 꺼내 더함
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    # 더한 값을 힙큐에 넣음 (새로 정렬한 카드 더미 추가)
    heapq.heappush(card, a+b)
    # 비교 횟수를 누적시킴
    result += a+b

print(result)
