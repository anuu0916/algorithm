# 2776 암기왕
import sys


def binary_search(start, end, target):
    while start <= end:
        mid = (start + end) // 2
        # 숫자를 찾았을 때
        if note1[mid] == target:
            return mid
        elif note1[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


t = int(input())

for i in range(t):
    n = int(input())
    note1 = list(map(int, sys.stdin.readline().split()))
    m = int(input())
    note2 = list(map(int, sys.stdin.readline().split()))

    note1.sort()

    for x in note2:
        # 숫자가 수첩1에 있는지 확인
        result = binary_search(0, n-1, x)
        if result is not None:
            print("1")
        else:
            print("0")
