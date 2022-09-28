# 14501 퇴사
import sys
n = int(input())
arr = []
dp = [0] * (n+1)

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))
    dp[i] = arr[i][1]

for i in range(n-1, -1, -1):
    if i+arr[i][0] <= n:
        dp[i] = max(arr[i][1] + dp[i+arr[i][0]], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
