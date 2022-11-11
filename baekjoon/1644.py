# 1644 소수의 연속합
import math
n = int(input())
a = [False, False] + [True] * (n-1)
prime = []

if n < 2:
    print(0)
    exit()

for i in range(2, n+1):
    if a[i]:
        prime.append(i)
        for j in range(i*2, n+1, i):
            a[j] = False

result = 0
start = 0
end = 0
while end <= len(prime):
    tmp = sum(prime[start:end])
    if tmp == n:
        result += 1
        end += 1
    elif tmp < n:
        end += 1
    else:
        start += 1

print(result)
