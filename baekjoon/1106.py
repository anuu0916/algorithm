# 1106 호텔
c, n = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [int(1e9)] * (c + 100)
# 0으로 초기화해 인원수와 고객 수가 같을 때 계산
dp[0] = 0
arr = sorted(arr, key = lambda x : x[0])

for cost, cus in arr:
    # 더 큰 인원수에서 최솟값을 가질 수 있으므로
    # 각 도시에서 얻을 수 있는 최대 고객의 수 100을 더해줌
    for i in range(cus, c + 100):
        dp[i] = min(dp[i], dp[i-cus] + cost)

print(min(dp[c:]))
