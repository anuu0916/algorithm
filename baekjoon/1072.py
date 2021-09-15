# 1072 게임
x, y = map(int, input().split())
z = y * 100 // x

# 승률이 99% 이상일 때 승률은 더 오르지 않음
if z >= 99:
    print("-1")
    exit()


# 정민언니 팁대로 함수로 풀어봄
# 파이썬은 함수가 더 빠르다고 하네요... (걍 시스템적 문제)
def binary_search(start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = (y + mid) * 100 // (x + mid)

        # 승률이 오르지 않는 경우 게임 수 올림
        if total <= z:  # 처음에 여기 등호 안넣었다가 계속 결과 1 나옴 ㅎㅎ
            start = mid + 1
        # 승률이 오른 경우 게임 수 낮춤
        else:
            result = mid
            end = mid - 1

    return result


print(binary_search(1, x))
