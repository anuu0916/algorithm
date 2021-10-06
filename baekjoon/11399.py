# 11399 ATM
import sys
n = int(input())
p = list(map(int, sys.stdin.readline().split()))

p.sort()  # 돈 인출 시간이 적은 순서대로 정렬
result = 0
s = 0

for i in range(n):
    # 0번째부터 i번째까지 시간 더함
    s += p[i]
    # i번째까지 누적한 합을 더함
    result += s

print(result)
