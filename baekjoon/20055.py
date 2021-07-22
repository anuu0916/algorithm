# 20055 컨베이어 벨트 위의 로봇
import sys

n, k = sys.stdin.readline().split()
n = int(n)
k = int(k)

if n < 2 or n > 100:
    exit()

if k < 1 or k > 2*n:
    exit()

a = list(map(int, input().split()))

for i in a:
    if i < 1 or i > 1000:
        exit()

r = [False for _ in range(2 * n)]
up = 0
down = n-1
cnt = 0
zero = 0

while zero < k:
    cnt += 1
    up -= 1
    down -= 1
    if up < 0:
        up = 2*n - 1
    if down < 0:
        down = 2*n - 1

    r[down] = False

    j = 0
    for i in range(1, n):
        index = down - i
        if index < 0:
            index = 2 * n - 1 - j
            j += 1

        next_index = (index + 1) % (2 * n)

        if r[index] is True and r[next_index] is False and a[next_index] > 0:
            if next_index == down:
                a[next_index] -= 1
                r[index] = False
                if a[next_index] == 0:
                    zero += 1
            else:
                r[index] = False
                r[next_index] = True
                a[next_index] -= 1
                if a[next_index] == 0:
                    zero += 1

    if a[up] > 0:
        r[up] = True
        a[up] -= 1
        if a[up] == 0:
            zero += 1


print(cnt)
