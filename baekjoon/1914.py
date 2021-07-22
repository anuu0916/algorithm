# 1914 하노이 탑
num = int(input())
print(2**num - 1)


def move(n, depart, arrive, via=0):
    if n == 1:
        print(depart, arrive)
    else:
        move(n-1, depart, via, arrive)
        print(depart, arrive)
        move(n-1, via, arrive, depart)


if num <= 20:
    move(num, 1, 3, 2)
