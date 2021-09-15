# 2343 기타 레슨
import sys
n, m = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))


def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = mid  # 블루레이 크기
        cnt = m  # 블루레이 개수

        # 강의 순서대로 녹화
        for x in arr:
            # 강의 크기만큼 차감시킴
            if total >= x:
                total -= x
            # 블루레이 용량 다 채웠을 경우
            else:
                total = mid
                cnt -= 1
                # 필요한 블루레이 개수가 m개를 넘어갈 경우
                if cnt <= 0 or x > mid:
                    cnt = -1
                    break
                else:
                    total -= x

        # 크기가 작아 강의를 다 녹화하지 못할 경우
        if cnt <= 0:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

    return result


print(binary_search(1, sum(arr)))
