# 13458 시험 감독
n = int(input())
arr = [0]
arr.extend(list(map(int, input().split())))

b, c = map(int, input().split())

result = 0
for i in range(1, n+1):
    check = arr[i]
    check -= b
    result += 1

    if check > 0:
        if check % c == 0:
            result += check // c
        else:
            result += (check // c) + 1

print(result)
