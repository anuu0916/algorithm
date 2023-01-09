# 두 개의 숫자열
T = int(input())

for test_case in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    answer = int(-1e5)
    if n > m:
        for i in range(n-m+1):
            tmp = 0
            for j in range(m):
                tmp += a[j+i] * b[j]
            answer = max(tmp, answer)
    else:
        for i in range(m-n+1):
            tmp = 0
            for j in range(n):
                tmp += a[j] * b[j+i]
            answer = max(tmp, answer)
    
    print("#%d %d" % (test_case, answer))
