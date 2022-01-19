# 14888 연산자 끼워넣기
import sys
from collections import deque

num = int(input())
a = list(map(int, sys.stdin.readline().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈 순서
operate = list(map(int, sys.stdin.readline().split()))
min_result = int(1e9)
max_result = int(-1e9)


# start : 다음 연산할 숫자 순서
# n : 지금까지 연산한 결과
# op : 남은 연산자 개수 배열
def bfs():
    queue = deque([[1, a[0], operate]])

    while queue:
        print(queue)
        start, n, op = queue.popleft()

        if op.count(0) == 4:
            global min_result, max_result
            min_result = min(min_result, n)
            max_result = max(max_result, n)

        for i in range(4):
            if op[i] <= 0:
                continue

            if i == 0:
                tmp = [op[0] - 1, op[1], op[2], op[3]]
                queue.append([start + 1, n + a[start], tmp])
            elif i == 1:
                tmp = [op[0], op[1] - 1, op[2], op[3]]
                queue.append([start + 1, n - a[start], tmp])
            elif i == 2:
                tmp = [op[0], op[1], op[2] - 1, op[3]]
                queue.append([start + 1, n * a[start], tmp])
            else:
                tmp = [op[0], op[1], op[2], op[3] - 1]
                queue.append([start + 1, n + a[start], tmp])


bfs()
print(max_result)
print(min_result)
