# 1759 암호 만들기
import sys
from itertools import combinations
l, c = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
result = []

for combi in combinations(arr, l):
    con = 0  # 자음
    vow = 0  # 모음
    for co in combi:
        if co in ['a', 'e', 'i', 'o', 'u']:
            vow += 1
        else:
            con += 1
    
    if con >= 2 and vow >= 1:
        result.append(''.join(sorted(combi)))


for res in sorted(result):
    print(res)
