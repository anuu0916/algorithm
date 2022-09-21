# 92335 k진수에서 소수 개수 구하기
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    num = ""

    if k != 10:
        while n > 0:
            n, mod = divmod(n, k)
            num += str(mod)

        num = num[::-1]
    else:
        num = str(n)

    # print(num)
    candidate = list(num.split("0"))
    # print(candidate)

    for c in candidate:
        if c == "1" or c == "":
            continue
        
        if is_prime(int(c)):
            answer += 1

    return answer

print(solution(110011, 10))