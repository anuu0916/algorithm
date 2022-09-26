from dateutil.relativedelta import relativedelta
from datetime import datetime

def solution(today, terms, privacies):
    t_date = list(map(int, today.split(".")))
    t_time = datetime(t_date[0], t_date[1], t_date[2])
    term = {}

    for i in range(len(terms)):
        tmp1, tmp2 = terms[i].split()
        term[tmp1] = int(tmp2)
    
    answer = []

    for i in range(len(privacies)):
        date, t = privacies[i].split()
        p_date = list(map(int, date.split(".")))

        p_date[2] -= 1
        if p_date[2] == 0:
            p_date[1] -= 1
            p_date[2] = 28

        if p_date[1] == 0:
            p_date[0] -= 1
            p_date[1] = 12

        p_time = datetime(p_date[0], p_date[1], p_date[2])
        delta = relativedelta(months=term[t])
        
        # print(p_time+delta)

        if (p_time + delta) < t_time:
            answer.append(i+1)
        
        # if term[t] + p_date[1] <= 12:
        #     p_date[1] += term[t]
        # else:
        #     p_date[0] += int((p_date[1] + term[t]) / 12)
        #     p_date[1] = (p_date[1] + term[t]) % 12
        
        # if p_date[0] < t_date[0]:
        #     answer.append(i+1)
        # elif p_date[0] == t_date[0] and p_date[1] < t_date[1]:
        #     answer.append(i+1)
        # elif p_date[0] == t_date[0] and p_date[1] == t_date[1] and p_date[2] < t_date[2]:
        #     answer.append(i+1)

    return answer
