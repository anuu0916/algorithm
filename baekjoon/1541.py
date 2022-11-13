# 1541 잃어버린 괄호
from collections import deque
expr = input().split('-')
num = []

for exp in expr:
    if exp == '':
        num.append(0)
        continue

    tmp = 0
    s = exp.split('+')
    for n in s:
        tmp += int(n)
    num.append(tmp)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)
