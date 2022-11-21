# 1717 집합의 표현
# 참고 : https://velog.io/@ashooozzz/Python-%EB%B6%84%EB%A6%AC%EC%A7%91%ED%95%A9-%EC%84%9C%EB%A1%9C%EC%86%8C%EC%A7%91%ED%95%A9

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(range(n+1))


# root를 찾는 함수
def find(num):
    # num 노드가 root가 아닐 때
    if arr[num] != num:
        # root 갱신 (낮은 깊이로 만들기 위해 arr[num]값 갱신)
        arr[num] = find(arr[num])
    return arr[num]


# 합집합 함수
def union(num1, num2):
    n1 = find(num1)
    n2 = find(num2)
    arr[n2] = n1


def isInclude(num1, num2):
    n1 = find(num1)
    n2 = find(num2)
    if n1 == n2:
        return True
    else:
        return False


for i in range(m):
    c, a, b = map(int, input().split())

    if c == 0:
        union(a, b)
    
    if c == 1:
        if isInclude(a, b):
            print("YES")
        else:
            print("NO")
