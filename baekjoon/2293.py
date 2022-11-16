# 2293 동전 1
# 참고 : https://mong9data.tistory.com/68
import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
dp = [0] * (k+1)
dp[0] = 1

for i in range(n):
    coin.append(int(sys.stdin.readline()))

for co in coin:
    for i in range(co, k+1):
        if i - co >= 0:
            # i원을 만드는 경우의 수 : co원 동전 + i-co원을 만드는 경우의수
            dp[i] += dp[i-co]

print(dp[k])
