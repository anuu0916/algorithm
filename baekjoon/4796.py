# 4796 캠핑
import sys
case = 0

while True:
    l, p, v = map(int, sys.stdin.readline().split())
    result = 0
    case += 1

    if l == 0 and p == 0 and v == 0:
        break

    # p를 주기로 l만큼 사용 가능
    result += (v // p) * l
    # p로 나눈 나머지 날이 l보다 클 때는 l만큼, 작을 때는 나머지 일만큼 사용 가능
    if v % p > l:
        result += l
    else:
        result += v % p

    print("Case {0}: {1}".format(case, result))
