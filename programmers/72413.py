# 72413 합승 택시 요금
INF = int(1e9)  # 무한을 의미하는 변수

def solution(n, s, a, b, fares):
    answer = 0
    # 최단 거리 테이블
    distance = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                distance[i][j] = 0

    # 연결 정보 입력
    for i in range(len(fares)):
        # u에서 v로 가는 가중치 w인 간선이 존재
        distance[fares[i][0]][fares[i][1]] = fares[i][2]
        distance[fares[i][1]][fares[i][0]] = fares[i][2]

    # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    answer = distance[s][a] + distance[s][b]
    for i in range(1, n + 1):
        new = distance[s][i] + distance[i][a] + distance[i][b]
        if new < answer:
            answer = new

    return answer


n = 6
s = 4
a = 5
b = 6
fares = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

print(solution(n, s, a, b, fares))