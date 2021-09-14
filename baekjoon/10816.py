# 10816 숫자 카드 2
import sys
n = int(input())
card = list(map(int, sys.stdin.readline().split()))
m = int(input())
target = list(map(int, sys.stdin.readline().split()))

card.sort()


# 어떻게 이진탐색으로 풀지?? 하다가 구글링했습니다
# upper bound - lower bound 를 하면 된다네요...
def upper_bound(num):
    start = 0
    end = n - 1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if card[mid] > num:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


def lower_bound(num):
    start = 0
    end = n - 1
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if card[mid] >= num:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result


for i in range(m):
    num = target[i]
    upper = upper_bound(num)
    if upper == 0 and card[n - 1] == num:
        upper = n
    lower = lower_bound(num)
    print(upper - lower, end=" ")
