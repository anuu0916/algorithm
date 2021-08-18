# 11722 가장 긴 감소하는 부분 수열
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
d = [0] * n
d[0] = 1

for i in range(1, n):
    d[i] = 1  # 1로 초기화
    for j in range(i):  # 앞에서부터 현재 수보다 큰 수를 찾음
        if a[i] < a[j]:
            d[i] = max(d[i], d[j] + 1)  # 감소하는 길이 중 가장 큰 값

print(max(d))
