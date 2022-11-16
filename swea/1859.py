# 1859 백만 장자 프로젝트
from collections import deque
t = int(input())

for test_case in range(1, t+1):
    n = int(input())
    price = deque(list(map(int, input().split())))

    most = price.pop()
    sell = 0
    buy = 0
    buy_cnt = 0
    while price:
        cur = price.pop()
        if cur > most:
            sell += most * buy_cnt
            buy_cnt = 0
            most = cur
        
        if cur < most:
            buy_cnt += 1
            buy += cur
    
    sell += most * buy_cnt
    
    print("#%d %d" % (test_case, sell-buy))
