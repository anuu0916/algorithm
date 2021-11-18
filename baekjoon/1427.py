# 1427 소트인사이드
import sys
arr = list(map(int, sys.stdin.readline().rstrip()))

arr.sort(reverse=True)
for n in arr:
    print(n, end="")
