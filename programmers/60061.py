# 60061 기둥과 보 설치

# 현재 설치된 구조물이 '가능한' 구조물인지 확인
def possible(answer):
    for x, y, stuff in answer:
        # 기둥인 경우
        if stuff == 0:
            # 바닥 위, 보의 한쪽 끝부분 위, 다른 기둥 위일 때만 가능
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            # 아니라면 return False 
            return False
        # 보인 경우
        elif stuff == 1:
            # 한쪽 끝부분이 기둥 위, 양쪽 끝부분이 다른 보와 동시에 연결될 때만 가능
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            # 아니라면 return False
            return False
    
    # 모든 조건을 만족할 경우
    return True


def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame

        # 구조물을 삭제할 경우
        if operate == 0:
            # 일단 삭제한 다음
            answer.remove([x, y, stuff])
            # 가능한 구조물인지 확인
            if not possible(answer):
                # 불가능하다면 다시 설치 (작업 무시)
                answer.append([x, y, stuff])
        
        # 구조물을 설치할 경우
        if operate == 1:
            # 일단 설치한 다음
            answer.append([x, y, stuff])
            # 가능한 구조물인지 확인
            if not possible(answer):
                # 불가능하다면 다시 삭제 (작업 무시)
                answer.remove([x, y, stuff])

    return sorted(answer)