# 3079 입국심사
# 구글링했습니다..
# X시간동안 한번 심사에 5초 걸리는 심사관이 검사할 수 있는 사람 수는 X/5명이다.
# 해당 방법을 기억하고, 각각의 심사관들이 X시간동안 검사할 수 있는 사람의 합이 전체 명수보다 크거나 같으면, 현재 가장 작은 시간과 비교하여, 작은 것을 result에 넣어주고, 최대크기는 mid값에서 1을 줄여준다.
# 그렇지 않으면, 정답일 가능성이 없기 때문에, 최소값에서 mid+1를 해주고, 다시 계산해준다.
# 최대값이 최소값보다 크거나 작을때까지 진행한다.
# https://velog.io/@kpg0518/%EB%B0%B1%EC%A4%80-3079%EB%B2%88-%EC%9E%85%EA%B5%AD%EC%8B%AC%EC%82%AC


n, m = map(int, input().split())
t = list()
for i in range(n):
    t.append(int(input()))

start = 0
end = max(t) * m

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2

    for x in t:
        total += mid // x
    if total >= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)
