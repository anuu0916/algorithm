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
    # start, n, op 순서대로 큐 삽입
    queue = deque([[1, a[0], operate]])

    while queue:
        start, n, op = queue.popleft()

        # 연산이 끝났을 때
        if op.count(0) == 4:
            global min_result, max_result
            # 최솟값과 최댓값 갱신
            min_result = min(min_result, n)
            max_result = max(max_result, n)
            continue

        # 모든 연산자에 대해
        for i in range(4):
            # 연산자 개수를 다 썼으면 건너뜀
            if op[i] <= 0:
                continue

            if i == 0:  # 덧셈
                tmp = [op[0] - 1, op[1], op[2], op[3]]
                queue.append([start + 1, n + a[start], tmp])
            elif i == 1:  # 뺄셈
                tmp = [op[0], op[1] - 1, op[2], op[3]]
                queue.append([start + 1, n - a[start], tmp])
            elif i == 2:  # 곱셈
                tmp = [op[0], op[1], op[2] - 1, op[3]]
                queue.append([start + 1, n * a[start], tmp])
            else:  # 나눗셈
                res = n // a[start]
                # 음수를 양수로 나눌 때
                # 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다. (문제 조건)
                if n < 0:
                    res = -n // a[start]
                    res = -res

                tmp = [op[0], op[1], op[2], op[3] - 1]
                queue.append([start + 1, res, tmp])


bfs()
print(max_result)
print(min_result)
