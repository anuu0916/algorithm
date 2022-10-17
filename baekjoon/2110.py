# 2110 공유기 설치
# 구글링했습니다..
import sys

n, c = map(int, sys.stdin.readline().split())
house = list()
for i in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()
start = 1
end = house[n - 1]

result = 0
while start <= end:
    cnt = 1
    mid = (start + end) // 2

    i = house[0]
    for x in house:
        if x - i >= mid:
            cnt += 1
            i = x

    if cnt < c:
        end = mid - 1
    else:
        result = max(result, mid)
        start = mid + 1

print(result)
