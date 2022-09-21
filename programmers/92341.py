# 92341 주차 요금 계산
import math

def cal_time(t1, t2):
    h1, m1 = map(int, t1.split(":"))
    h2, m2 = map(int, t2.split(":"))
    
    return (h2*60 + m2) - (h1*60 + m1)

def cal_fee(total_time, std_time, std_fee, unit_time, unit_fee):
    if total_time <= std_time:
        return std_fee
    else:
        return std_fee + math.ceil((total_time - std_time) / unit_time) * unit_fee

def solution(fees, records):
    answer = []
    dic = {}
    total_time = {}

    for r in records:
        t, car, status = r.split()
        if status == "IN":
            dic[car] = t
        else:
            min = cal_time(dic[car], t)
            dic[car] = 0
            if car in total_time:
                total_time[car] += min
            else:
                total_time[car] = min
    
    for car in dic:
        if dic[car] != 0:
            if car not in total_time:
                total_time[car] = 0
            total_time[car] += cal_time(dic[car], "23:59")

    total_time = sorted(total_time.items())

    for i in range(len(total_time)):
        fee = cal_fee(total_time[i][1], fees[0], fees[1], fees[2], fees[3])

        answer.append(fee)

    return answer


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
print(solution(fees, records))