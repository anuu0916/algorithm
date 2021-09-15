# 2512 예산
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
m = int(input())

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in arr:
        # 예산 총액 계산
        if x > mid:
            total += mid
        else:
            total += x
    # 예산이 부족한 경우 상한액 낮춤
    if total > m:
        end = mid - 1
    # 예산이 남는 경우 상한액 높임
    else:
        result = mid
        start = mid + 1

print(result)
