# 14725 개미굴
import sys
input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    tmp = list(input().split())
    arr.append(tmp[1:])

arr.sort()
answer = []
dash = "--"

for i in range(n):
    if i == 0:
        for j in range(len(arr[i])):
            answer.append(dash*j+arr[i][j])
    else:
        idx = 0
        for j in range(len(arr[i])):
            if len(arr[i-1]) <= j or arr[i][j] != arr[i-1][j]:
                break
            else:
                idx = j+1
        for j in range(idx, len(arr[i])):
            answer.append(dash*j+arr[i][j])

for ans in answer:
    print(ans)