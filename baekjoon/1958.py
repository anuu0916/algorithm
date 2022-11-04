# 1958 LCS 3
st1 = input().rstrip()
st2 = input().rstrip()
st3 = input().rstrip()

dp = [[[0] * (len(st3)+1) for _ in range(len(st2)+1)] for _ in range(len(st1)+1)]

for i in range(1, len(st1)+1):
    for j in range(1, len(st2)+1):
        for k in range(1, len(st3)+1):
            if st1[i-1] == st2[j-1] and st2[j-1] == st3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])
