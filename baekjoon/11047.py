# 11047 동전 0
n, k = map(int, input().split())
coin = []
count = 0  # 동전의 개수를 저장할 변수

# 동전의 가치 입력받음
for i in range(n):
    coin.append(int(input()))

# 동전의 가치가 오름차순으로 주어지므로 뒤에서부터 계산
for i in range(n-1, -1, -1):
    count += k // coin[i]  # k원에서 현재 단위만큼 나눈 몫을 더함
    k %= coin[i]  # 나머지를 구해 다음 단위에서 계산함

print(count)
