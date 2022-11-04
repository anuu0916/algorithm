# 5582 공통 부분 문자열
s1 = input().rstrip()
s2 = input().rstrip()
dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
longest = 0
cnt = 0

for i in range(1, len(s1)+1):
    for j in range(1, len(s2)+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            longest = max(longest, dp[i][j])

print(longest)

# print('  0  '+'  '.join(s2))
# tmp = '0'+s1
# for i in range(len(dp)):
#     print(tmp[i], dp[i])
