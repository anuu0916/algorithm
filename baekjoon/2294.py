# 2294 동전 2
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coin = []
dp = [10001] * (k+1)
dp[0] = 0

for i in range(n):
    tmp = int(input())
    coin.append(tmp)

for co in coin:
    for i in range(co, k+1):
        dp[i] = min(dp[i], dp[i-co]+1)

if dp[k] >= 10001:
    print(-1)
else:
    print(dp[k])
