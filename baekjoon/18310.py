# 18310 안테나
import sys
n = int(input())
home = list(map(int, sys.stdin.readline().split()))
home.sort()

# 가운데에 위치한 집에 안테나 설치
# 답으로 여러 개가 나올 때, 몫 나누기 // 를 사용하면 자동으로 작은 값 나옴
print(home[(n-1) // 2])
