# 92334 신고 결과 받기

def solution(id_list, report, k):
    answer = []
    dic = {}
    email = {}

    for i in id_list:
        dic[i] = set([])
        email[i] = 0
    
    for r in report:
        reporter, reported = r.split()
        dic[reported].add(reporter)
    
    for d in dic:
        if len(dic[d]) >= k:
            for i in dic[d]:
                email[i] += 1
    
    for e in email:
        answer.append(email[e])

    return answer


id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
print(solution(id_list, report, k))