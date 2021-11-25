# 5052 전화번호 목록
t = int(input())


# 구글링함...
# 정렬했으니까 앞뒤 숫자만 비교해도 다 찾을 수 있다!
def check_num():
    n = int(input())
    numbers = []
    check = 0
    for i in range(n):
        numbers.append(input())

    numbers.sort()
    # 틀린 이유... 그냥 포함관계가 아니라 "접두어"여야 한다!!
    for i in range(n-1):
        length = len(numbers[i])
        if numbers[i] in numbers[i+1][:length]:
            check = 1
            break

    if check == 1:
        print("NO")
    else:
        print("YES")


# 그냥 파이썬 특성상 함수 쓰면 빠르다니까 함수로 해줌
for _ in range(t):
    check_num()
