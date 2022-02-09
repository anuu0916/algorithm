# 18428 감시 피하기
import sys
import copy
from itertools import combinations

n = int(input())
arr = []  # 복도의 정보
teacher = []  # 선생님 위치
space = []

for i in range(n):
    tmp = list(sys.stdin.readline().split())
    arr.append(tmp)
    for j in range(n):
        if tmp[j] == "T":
            teacher.append([i, j])
        if tmp[j] == "X":
            space.append([i, j])


# 특정 방향으로 감시 진행
# 학생을 발견할 경우 True 리턴, 발견하지 않을 경우 False 리턴
def watch(x, y, direction):
    # 왼쪽 방향 감시
    if direction == 0:
        while y >= 0:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            y -= 1
    # 오른쪽 방향 감시
    if direction == 1:
        while y < n:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            y += 1
     # 위쪽 방향 감시
    if direction == 2:
        while x >= 0:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            x -= 1
     # 아래쪽 방향 감시
    if direction == 3:
        while x < n:
            if arr[x][y] == "S":
                return True
            if arr[x][y] == "O":
                return False
            x += 1
    return False


# 장애물 설치 후 선생님이 학생을 발견할 수 있는지 검사
def process():
    for x, y in teacher:
        for d in range(4):
            if watch(x, y, d):
                return True
    return False


# 빈 공간의 모든 조합에 대해
for data in combinations(space, 3):
    # 장애물 설치하기
    for x, y in data:
        arr[x][y] = "O"
    
    # 학생을 발견할 수 있는지 검사
    if not process():
        print("YES")
        exit()
    
    # 장애물 다시 없애기
    for x, y in data:
        arr[x][y] = "X"

print("NO")
