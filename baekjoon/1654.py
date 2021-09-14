# 1654 랜선 자르기
k, n = map(int, input().split())
line = list()

for i in range(k):
    line.append(int(input()))  # append 시간복잡도 O(1)

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(line)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    if mid < 1:
        mid = 1

    for x in line:
        # 잘랐을 때의 랜선의 개수 계산
        if x >= mid:
            total += x // mid
    # 랜선의 개수가 부족한 경우 자를 랜선의 길이를 줄임
    if total < n:
        end = mid - 1
    # 랜선의 개수가 n보다 클 경우 자를 랜선의 길이를 높임
    else:
        result = mid  # 더 많이 만들었어도 n개 만든거니까 일단 기록
        start = mid + 1

print(result)
