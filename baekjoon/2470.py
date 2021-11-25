# 2470 두 용액
import sys
n = int(input())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

# 구글링했습니다...
# 투포인터를 사용하라고 하더라고요,,
left = 0
right = n-1

result = []
total = abs(liquid[left] + liquid[right])

while left < right:
    tot = liquid[left] + liquid[right]
    # 처음에 등호 안넣어줬다가 indexError 나서 틀림...
    # n이 2일 때 등호가 없으면 result에 아무것도 안들어가서 틀린다
    if abs(tot) <= total:
        total = abs(tot)
        result = [liquid[left], liquid[right]]

    # 합이 음수라면 left를 늘려 더 큰 값을 더해 0에 가깝게 만든다
    if tot < 0:
        left += 1
    # 합이 양수라면 right를 줄여 더 작은 값을 더해 0에 가깝게 만든다
    else:
        right -= 1

print(result[0], result[1])
