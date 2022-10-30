# 1747 소수&팰린드롬
import math
n = int(input())

if n == 1:
    print(2)
    exit()


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True


while True:
    strn = str(n)
    if strn == strn[::-1]:
        if is_prime(n):
            print(n)
            break
    
    n += 1
