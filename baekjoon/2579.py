# 2579 계단 오르기
n = int(input())
stair = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(1, n + 1):
    stair[i] = int(input())

    if i == 1:
        d[i] = stair[i]
    else:
        d[i] = max(d[i-3] + stair[i-1], d[i-2]) + stair[i]

print(d[n])
