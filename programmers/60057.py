# 60057 문자열 압축

def solution(s):
    # 문자열의 길이
    length = len(s)
    # 압축이 하나도 되지 않았을 때가 최대 압축 값
    answer = length

    # 문자열을 자를 수 있는 경우의 수는 1개부터 문자열의 절반까지
    for i in range(1, length//2 + 1):
        st = s[0:i] # 처음 시작하는 문자 단위 묶음
        repeat = 1 # 반복 횟수
        tmp = 0 # 압축 길이

        # 두 번째 단위 묶음부터 문자열의 끝까지 압축 단위 길이만큼 건너뛰며 반복
        for j in range(i, length+i, i):
            # 현재 문자 단위 묶음과 다음 문자 단위 묶음이 같을 때
            # 즉, 같은 문자열이 반복될 경우
            if st == s[j:j+i]:
                repeat += 1 # 반복 횟수 증가
            
            # 문자열이 반복되지 않을 경우
            else:
                if repeat == 1: # 한 번 반복할 때는 숫자 생략
                    tmp += len(st)
                # 두 번 이상 반복할 경우 숫자 포함
                else:
                    tmp += len(st) + len(str(repeat))
                
                # 다음 문자열로 이동
                st = s[j:j+i]
                # 반복 횟수 초기화
                repeat = 1

        # 가장 작은 압축 길이 계산
        answer = min(answer, tmp)

    return answer

print(solution("aabbaccc"))