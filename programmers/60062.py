# 60062 외벽 점검
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려 원형 벽을 선형으로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    
    # 투입할 친구의 최솟값을 비교해야 하므로 최대값보다 1 큰 수로 초기화
    answer = len(dist) + 1

    # 취약 지점을 각각 시작점으로 설정 (start : 취약 지점의 인덱스)
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수에 대해 반복
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수

            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            
            # 시작점부터 모든 취약 지점 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 투입할 친구 수 증가
                    # 친구를 더 투입할 수 없을 경우
                    if count > len(dist):
                        break

                    # 현재 위치에서 시작해 새로운 친구가 점검할 수 있는 마지막 위치 계산
                    position = weak[index] + friends[count - 1]
            
            # 투입한 친구의 최솟값 갱신
            answer = min(answer, count)
    
    # 모든 친구를 투입해도 점검할 수 없는 경우
    if answer > len(dist):
        return -1
    else:
        return answer