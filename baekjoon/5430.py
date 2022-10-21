# 5430 AC
from collections import deque
T = int(input())


def function(p, arr):
    rvs = False
    for j in range(len(p)):
        if p[j] == 'R':
            if not rvs:
                rvs = True
            else:
                rvs = False
        elif p[j] == 'D':
            if len(arr) > 0:
                if not rvs:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                print("error")
                return

    if rvs:
        arr.reverse()
    print("["+",".join(map(str, arr)) + "]")
    return


for test_case in range(T):
    p = input()  # 함수
    n = int(input())  # 배열에 들어있는 수의 개수
    inarr = input()
    inarr = inarr[1:-1]
    arr = deque([])

    if n > 0:
        arr.extend(list(map(int, inarr.split(','))))

    function(p, arr)
