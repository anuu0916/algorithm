# 1463 1로 만들기
# 책을 참고했습니다 ㅎㅎ
n = int(input())

# 인덱스 크기를 충분히 크게 설정합시다...
d = [0] * (10 ** 6 + 1)

for i in range(2, n + 1):
    d[i] = d[i-1] + 1

    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)

print(d[n])
