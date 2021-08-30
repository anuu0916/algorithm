# 2805 나무 자르기
# 떡볶이 떡 만들기 문제랑 똑같다..!
import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(tree)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in tree:
        # 잘랐을 때의 나무의 길이 계산
        if x > mid:
            total += x - mid
    # 나무의 길이가 부족한 경우 절단기 높이 낮춤
    if total < m:
        end = mid - 1
    # 나무의 길이가 넘치는 경우 절단기 높이 높임
    else:
        result = mid  # 최대한 덜 잘랐을 때의 길이를 구하기 위해 result에 기록
        start = mid + 1

print(result)
