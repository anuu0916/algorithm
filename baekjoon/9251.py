# 9251 LCS
# 참고 : https://melonicedlatte.com/algorithm/2018/03/15/181550.html

st1 = input().rstrip()
st2 = input().rstrip()
dp = [[0] * (len(st1)+1) for _ in range(len(st2)+1)]

for i in range(1, len(st2)+1):
    for j in range(1, len(st1)+1):
        if st1[j-1] == st2[i-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
