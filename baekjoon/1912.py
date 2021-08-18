# 1912 연속합
# 구글링했습니다...ㅎㅎ
import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
d = [0] * n  # 누적합 저장할 배열
d[0] = arr[0]

for i in range(1, len(arr)):
    if d[i-1] > 0:
        d[i] = arr[i] + d[i-1]
    else:  # d[i-1]이 음수면 선택하지 않고 넘어감. 현재 수부터 시작
        d[i] = arr[i]

print(max(d))
