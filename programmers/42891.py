# 42891 무지의 먹방 라이브
from collections import deque
import heapq
food_times = [3, 1, 2]
k = 5
length = len(food_times)
deq = deque()


def solution():
    answer = 0
    # 최소 몇 바퀴 돌 수 있는지
    turn = int(k / length)
    # 한 음식을 다 먹을 때 까지 or 최대 회전할 수 있는 만큼 먹기 (빼기)
    n = min(min(food_times), turn)
    for i in range(length):
        # 다 먹었으면 제외시킴
        if food_times[i] - n == 0:
            continue
        deq.append([food_times[i] - n, i + 1])

    # print(deq)
    # n바퀴 순회하고 장애까지 남은 시간
    remain = k - n * length
    # print(remain)

    # 남은 시간 동안
    while deq and remain > 0:
        # 다 먹었으면 제외시킴
        if deq[0][0] - 1 == 0:
            deq.popleft()
            remain -= 1
            continue
        deq[0] = [deq[0][0] - 1, deq[0][1]]
        # print(remain, deq)
        # 회전
        deq.rotate(-1)
        remain -= 1

    # print(deq)
    if deq:
        answer = deq[0][1]
    else:  # 더 섭취해야할 음식이 없을 때
        answer = -1
    return answer


def solution2(k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))

    food_num = len(food_times)  # 남은 음식 개수
    previous = 0  # 이전에 제거한 음식을 다 먹는 데 걸리는 시간

    while h:
        # 현재 음식을 다 먹는 데 걸리는 시간 :
        # (현재 음식의 food_time - previous) * 남은 음식의 개수
        # 다시 말해서, 현재 음식의 남은 food_time 번 만큼 회전하는 데 걸리는 시간
        t = (h[0][0] - previous) * food_num

        # 시간이 남을 경우 현재 음식 다 먹기
        if k >= t:
            k -= t
            previous = heapq.heappop(h)[0]
            food_num -= 1
        # 현재 음식을 다 먹을 시간이 없을 경우
        else:
            # 시간이 가장 짧게 걸리는 음식도 다 못 먹으니
            # 최대로 회전할 수 있을 만큼 회전시켜도 food_num은 그대로임
            # 따라서 k % food_num 번째 음식이 정답
            idx = k % food_num
            # 인덱스를 기준으로 힙 정렬
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break

    return answer


print(solution2(k))
