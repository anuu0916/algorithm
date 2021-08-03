# 11726 2xn 타일링
n = int(input())

d = [0] * 1001
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    # 처음엔 이런식으로 생각함... 그런데 겹치는 경우의 수가 있더라고요
    # for j in range(1, i//2 + 1):
    #     d[i] += d[i-j] + d[j]

    # 그래서 구글링했습니다ㅠ
    # 맨 오른쪽을 2x1타일 1개로 고정하는 경우의 수 + 1x2 타일 2개로 고정하는 경우의 수
    d[i] = (d[i-1] + d[i-2]) % 10007

print(d[n])
