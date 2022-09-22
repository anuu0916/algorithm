# 72412 순위 검색


def solution(info, query):
    answer = []
    info_words = []
    for i in range(len(info)):
        tmp = info[i].split()
        info_words.append(tmp)
    
    for i in range(len(query)):
        words = query[i].split(" and ")
        tmp = words.pop().split()
        words.extend(tmp)
        
        cnt = 0
        for j in range(len(info)):
            for k in range(5): # len(words)
                if k < 4:
                    if info_words[j][k] != words[k] and words[k] != '-':
                        break
                else:
                    if int(info_words[j][k]) >= int(words[k]):
                        cnt += 1
        
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))