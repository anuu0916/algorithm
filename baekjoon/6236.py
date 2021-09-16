# 6236 용돈 관리
n, m = map(int, input().split())
arr = list()
for i in range(n):
    arr.append(int(input()))


def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2  # 인출할 돈 단위 k
        total = mid  # 인출한 돈
        cnt = m  # 인출 횟수

        # 날짜 순서대로 용돈 사용
        for x in arr:
            # 돈 액수만큼 차감시킴
            if total >= x:
                total -= x
            # 돈이 모자랄 경우
            else:
                total = mid
                cnt -= 1
                # 인출 횟수가 m번을 넘어가거나 하루에 쓸 돈이 k보다 클 경우
                if cnt <= 0 or x > mid:
                    cnt = -1
                    break
                else:
                    total -= x

        # 쓸 돈보다 인출할 돈이 작을 경우
        if cnt <= 0:
            start = mid + 1
        else:
            result = mid
            end = mid - 1

    return result


print(binary_search(1, sum(arr)))
