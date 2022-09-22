# 72411 메뉴 리뉴얼
from itertools import combinations

def solution(orders, course):
    answer = []
    
    for num in course:
        combi = []
        for order in orders:
            tmp = list(combinations(order, num))
            tmp_list = []
            for t in tmp:
                t = list(t)
                t.sort()
                tmp_list.append(t)
            combi.extend(tmp_list)

        maximum = 2
        max_order = []
        for c in combi:
            if c in max_order:
                continue
            cnt = combi.count(c)
            if cnt > maximum:
                max_order = [c]
                maximum = cnt
            elif cnt == maximum:
                max_order.append(c)
        
        answer.extend(max_order)
    
    result = []
    for ans in answer:
        str = ""
        for a in ans:
            str += a
        result.append(str)

    return sorted(result)

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
