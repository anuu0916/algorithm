# 6603 로또
import sys
from itertools import combinations
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    k = arr.pop(0)

    if len(arr) == 0 and k == 0:
        break

    combi = list(combinations(arr, 6))
    combi.sort()

    for co in combi:
        print(*co)
    
    print()
    