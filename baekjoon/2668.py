# 2668 숫자 고르기
from itertools import combinations
n = int(input())
arr = [0]
result = set()

for i in range(n):
    arr.append(int(input()))


def dfs(first, second, num):
    first.add(num)
    second.add(arr[num])
    if arr[num] in first:
        if first == second:
            result.update(first)
        return
    return dfs(first, second, arr[num])


for i in range(1, n+1):
    if i not in result:
        dfs(set(), set(), i)

print(len(result))
for res in sorted(result):
    print(res)
