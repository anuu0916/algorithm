# 9663 N-Queen
# 백트래킹
# 구글링했습니다...

n = int(input())
col = [0] * n
result = 0


def check(depth):
    # 퀸을 놓을 수 있는지 검사
    for j in range(depth):
        if col[depth] == col[j]:
            return False
        elif abs(depth - j) == abs(col[depth] - col[j]):
            return False

    return True


def nqueen(depth):
    global result
    if depth == n:
        result += 1
        return

    for i in range(n):
        col[depth] = i

        if check(depth):
            nqueen(depth+1)


nqueen(0)
print(result)
