# 1913 달팽이
n = int(input())
find = int(input())
# 0으로 채워진 nXn 배열 만듦
res = [[0 for col in range(n)] for row in range(n)]

col = -1  # 0부터 시작했더니 그 변의 끝까지 가질 않아서,, -1부터 시작
row = 0
cnt = 0
i = n**2


# 배열 출력 함수
def print_array():
    for row in res:
        for item in row:
            print(item, end=" ")
        print()


# n**2번부터 1번까지 큰 수부터 배열에 저장
# 1번 : 1만큼 아래로
# 2번 : 1만큼 오른쪽으로
# 3번 : 1만큼 위로
# 4번 : 1만큼 왼쪽으로
# 다음 칸이 0이 아니거나, 배열 밖을 벗어나면 다음 순서
while i > 0:
    if cnt % 4 == 0:
        while col + 1 < n and res[col+1][row] == 0:
            col += 1
            res[col][row] = i
            i -= 1
    elif cnt % 4 == 1:
        while row + 1 < n and res[col][row+1] == 0:
            row += 1
            res[col][row] = i
            i -= 1
    elif cnt % 4 == 2:
        while col - 1 >= 0 and res[col - 1][row] == 0:
            col -= 1
            res[col][row] = i
            i -= 1
    elif cnt % 4 == 3:
        while row - 1 >= 0 and res[col][row - 1] == 0:
            row -= 1
            res[col][row] = i
            i -= 1

    cnt += 1


print_array()

# 찾을 숫자의 위치 찾기
# 원래 입력할 숫자가 찾을 숫자면 그 인덱스를 따로 저장할까 하다가...
# if문을 매번 쓰기가 싫어서 (저는 짧은 코드를 좋아합니다) 마지막에 반복문으로 찾았습니다
# 복잡도는 이게 더 안좋을지도...
for i in range(n):
    if find in res[i]:
        print(i+1, res[i].index(find)+1)
