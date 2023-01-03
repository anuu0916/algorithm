# 1961 숫자 배열 회전
import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input().split()))
    
    arr90 = list(zip(*arr[::-1]))
    arr180 = list(zip(*arr90[::-1]))
    arr270 = list(zip(*arr180[::-1]))

    print("#%d" % test_case)
    for i in range(n):
        tmp = "".join(arr90[i]) + " " + "".join(arr180[i]) + " " + "".join(arr270[i])
        print(tmp)
    
