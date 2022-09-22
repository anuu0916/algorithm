# 72410 신규 아이디 추천
import re

def solution(new_id):
    # 1단계
    answer = new_id.lower()
    print(answer)

    # 2단계
    answer = re.sub("[^a-z0-9-_.]", "", answer)
    print(answer)

    # 3단계
    tmp = answer[0]
    for i in range(1, len(answer)):
        if tmp[-1] == '.' and answer[i] == '.':
            continue
        else:
            tmp += answer[i]
    
    answer = tmp
    print(answer)

    # 4단계
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if len(answer) == 0:
        answer = "a"
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if len(answer) > 0 and answer[-1] == '.':
        answer = answer[:-1]
    
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))