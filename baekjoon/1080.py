# 1080 행렬
n, m = map(int, input().split())
A = []
B = []
count = 0

for i in range(n):
    A.append(list(map(int, input())))

for i in range(n):
    B.append(list(map(int, input())))

# 행렬이 같으면 0 출력
# 이 때, 행렬이 3x3보다 작아도 0을 출력하게 됨
if A == B:
    print(0)
    exit()


# 3x3만큼 뒤집음
def invert(i, j):
    for k in range(3):
        for l in range(3):
            A[i + k][j + l] += 1
            A[i + k][j + l] %= 2


# 3x3만큼 뒤집을 수 있는 범위 안에서 반복
# A의 원소와 B의 원소가 다르면 거기서부터 3x3만큼 뒤집음
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            invert(i, j)
            count += 1

if A == B:
    print(count)
else:
    print(-1)
