# 2800 괄호 제거
import sys
from collections import deque
from itertools import combinations
expr = list(sys.stdin.readline().strip())

stack = deque([])
pair = []
result = set()

for idx, word in enumerate(expr):
    if word == '(':
        stack.append(idx)

    if word == ')':
        pair.append((stack.pop(), idx))

for i in range(1, len(pair)+1):
    c = combinations(pair, i)

    for j in c:
        tmp = expr[:]
        for k in j:
            tmp[k[0]] = ""
            tmp[k[1]] = ""
        result.add(''.join(tmp))

for res in sorted(result):
    print(res)
