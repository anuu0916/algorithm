# 15486 퇴사 2
import sys
n = int(input())
consult = list()
d = [0] * (n + 2)
cur = 0

for i in range(n):
    consult.append(list(map(int, sys.stdin.readline().split())))

# 구글링함.... 너무 어렵네요...
# 뒤에서부터 시작
# d[i] : i일 까지의 최대 수익
for i in range(n, 0, -1):
    pt = i + consult[i-1][0]  # 현재 날짜 + 상담 완료에 걸리는 기간
    if pt > n + 1:  # n보다 크면 상담을 하지 못함
        d[i] = d[i + 1]  # 다음 날짜의 수익이 현재 날짜의 최대 수익
    else:
        # 이 날짜의 상담을 하지 않을 경우, 상담을 할 경우 중 더 큰 값
        # 상담을 하지 않을 때 = d[i + 1]
        # 상담을 할 때 = 현재 상담 수익 + 상담이 끝나고 나서 수익
        d[i] = max(d[i + 1], consult[i-1][1] + d[pt])

print(d[1])
