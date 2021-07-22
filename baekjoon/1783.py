# 1783 병든 나이트
move = [[2, 1], [1, 2], [-1, 2], [-2, 1]]
start = [1, 1]
cnt = 1

n, m = input().split()
n = int(n)
m = int(m)

# 구글링했습니다... 뒤지고싶네
if n == 1:
    print(cnt)
elif n < 3:
    print(4 if 4 < int((m+1)/2) else int((m+1)/2))
elif m < 7:
    print(4 if 4 < m else m)
else:
    cnt += m-3
    print(cnt)
