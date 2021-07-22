# 20923 숫자 할리갈리 게임
import sys
from collections import deque
# 덱
do = deque()
su = deque()
# 그라운드
dg = deque()
sg = deque()

n, m = sys.stdin.readline().split()
n = int(n)
m = int(m)

# 도도, 수연이의 덱 입력
for i in range(n):
    d, s = sys.stdin.readline().split()
    do.append(int(d))
    su.append(int(s))


# 종을 칠 수 있는지 판별하는 함수
def bell():
    # 도도가 종을 칠 경우
    if (len(dg) != 0 and dg[len(dg)-1] == 5) or (len(sg) != 0 and sg[len(sg)-1]) == 5:
        do.extendleft(sg)
        do.extendleft(dg)
        sg.clear()
        dg.clear()
    # 수연이가 종을 칠 경우
    elif len(dg) != 0 and len(sg) != 0 and dg[len(dg)-1] + sg[len(sg)-1] == 5:
        su.extendleft(dg)
        su.extendleft(sg)
        sg.clear()
        dg.clear()


# m번 반복
for i in range(m):
    # 0번부터 짝수번째에 도도가 카드를 냄
    if i % 2 == 0:
        dg.append(do.pop())
        if len(do) == 0:
            print("su")
            exit()
    # 홀수 번째에 수연이가 카드를 냄
    else:
        sg.append(su.pop())
        if len(su) == 0:
            print("do")
            exit()

    bell()

if len(do) > len(su):
    print("do")
elif len(do) < len(su):
    print("su")
else:
    print("dosu")
