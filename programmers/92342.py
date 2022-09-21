# 92342 양궁대회
from itertools import combinations

def cal_score(apeach, ryan):
    a_score = 0
    r_score = 0

    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue

        if apeach[i] >= ryan[i]:
            a_score += 10-i
        else:
            r_score += 10-i


    return r_score - a_score


def solution(n, info):
    answer = []
    arr = []
    
    for i in range(11):
        if info[i] < n:
            arr.extend([10-i] * (info[i] + 1))
    
    combi = list(combinations(arr, n))

    max_diff = -1
    for c in combi:
        temp  = []
        for i in range(11):
            temp.append(c.count(10-i))

        curr = cal_score(info, temp)
        if curr >= max_diff :

            if answer != [] and curr == max_diff:
                for i in range(11):
                    if temp[10-i] > answer[10-i]:
                        answer = temp
                        break
                    elif temp[10-i] < answer[10-i]:
                        break
            else:
                max_diff = curr
                answer = temp

    if len(answer) == 0 or max_diff <= 0:
        return [-1]
    else:
        return answer

print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))