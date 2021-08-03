# 2579 계단 오르기
n = int(input())
stair = [0] * (n + 1)
d = [0] * (n + 1)

for i in range(1, n + 1):
    stair[i] = int(input())

    if i == 1:
        d[i] = stair[i]
    else:
        # i번째 계단 최대 점수 =
        # i-2번째까지 최대 점수 + i번째 점수, i-3번째까지 최대 점수 + i-1번째 점수 + i번째 점수
        # 3칸을 연속으로 오르는 경우를 방지하기 위해,
        # d[i-1]과 비교하는게 아니라 d[i-3] + stair[i-1]과 비교함
        # 둘 중 더 큰 값이 최대 점수
        d[i] = max(d[i-3] + stair[i-1], d[i-2]) + stair[i]

print(d[n])
