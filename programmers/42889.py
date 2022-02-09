# 42889 실패율

def solution(N, stages):
    failure = []
    stages.sort()
    # 스테이지에 도달한 플레이어 수
    reached = len(stages)

    for i in range(1, N+1):
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        fail_num = stages.count(i)

        # 도달한 플레이어가 없을 때
        if reached == 0:
            failure.append((0, i))
        else:
            failure.append((fail_num/reached, i))
        
        # 다음 스테이지에 도달한 플레이어 수 계산
        reached -= fail_num
    
    # 실패율이 높은 순서대로, 실패율이 같다면 스테이지 번호가 작은 순서대로 정렬
    failure.sort(key=lambda x: (-x[0], x[1]))
    
    # 스테이지 번호만 따로 배열에 넣어 리턴
    answer = []
    for f in failure:
        answer.append(f[1])
    return answer


N = 4
stages =[4,4,4,4,4]
print(solution(N, stages))