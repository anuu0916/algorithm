# 15686 치킨 배달
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
data = []
chicken = [] # 치킨집 위치
home = [] # 집 위치

# 위치 정보 입력
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    data.append(tmp)
    for j in range(n):
        if tmp[j] == 2:
            chicken.append((i, j))
        elif tmp[j] == 1:
            home.append((i, j))

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidates):
    result = 0
    # 모든 집에 대해
    for hx, hy in home:
        # 가장 가까운 치킨집 찾음
        tmp = int(1e9)
        for cx, cy in candidates:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집 거리 더함
        result += tmp
    # 치킨 거리 반환
    return result

# 치킨 거리의 합의 최솟값 출력
result = int(1e9)
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
