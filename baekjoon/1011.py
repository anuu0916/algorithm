# 1011 Fly me to the Alpha Centauri
# 참고 : https://eunhee-programming.tistory.com/99
T = int(input())

for test_case in range(T):
    x, y = map(int, input().split())
    d = y - x
    n = 0

    while True:
        if d <= n*(n+1):
            break
        n += 1
    
    if d <= n**2:
        print(n*2-1)
    else:
        print(n*2)
