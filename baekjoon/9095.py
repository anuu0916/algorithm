# 9095 1, 2, 3 더하기
d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

t = int(input())

for i in range(t):
    n = int(input())

    if d[n] != 0:
        print(d[n])
    else:
        for j in range(4, n + 1):
            # 첫 번째 수 1로 고정 + 2로 고정 + 3으로 고정
            d[j] = d[j-1] + d[j-2] + d[j-3]

        print(d[n])
