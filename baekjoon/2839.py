# 2839 설탕 배달
import sys
input = sys.stdin.readline
n = int(input())
answer = 0

while n >= 0:
    if n % 5 == 0:
        answer += n // 5
        print(answer)
        break
    
    n -= 3
    answer += 1
else :
    print(-1)
