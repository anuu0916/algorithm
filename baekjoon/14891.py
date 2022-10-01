# 14891 톱니바퀴
import sys
from collections import deque

gear = []

for i in range(4):
    tmp = list(sys.stdin.readline())
    tmp.pop()  # 개행문자 제거
    tmp = list(map(int, tmp))
    gear.append(deque(tmp))


k = int(input())
turn = []
for i in range(k):
    turn.append(list(map(int, sys.stdin.readline().split())))


# 톱니바퀴는 2번이랑 6번 마주봄
for tu in turn:
    num = tu[0] - 1
    ro = tu[1]
    check = [0, 0, 0, 0]  # 회전 표시 배열
    check[num] = ro

    # 오른쪽으로 확인
    for i in range(3-num):
        if check[num+i] != 0:
            if gear[num+i][2] != gear[num+i+1][6]:
                check[num+i+1] = -check[num+i]
    
    # 왼쪽으로 확인
    for i in range(num):
        if check[num-i] != 0:
            if gear[num-i][6] != gear[num-i-1][2]:
                check[num-i-1] = -check[num-i]
    

    for i in range(4):
        gear[i].rotate(check[i])


result = 0
for i in range(4):
    result += gear[i][0] * (2**i)

print(result)
