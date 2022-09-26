def solution(cap, n, deliveries, pickups):
    answer = 0

    while True:
        deli = 0
        pick = 0
        dis = -1
        for i in range(n-1, -1, -1):
            if dis < i and (deliveries[i] > 0 or pickups[i] > 0):
                dis = i+1
                n = dis
            
            if deli + deliveries[i] > cap:
                deliveries[i] -= (cap - deli)
                deli = cap
            else:
                deli += deliveries[i]
                deliveries[i] = 0
            
            if pick + pickups[i] > cap:
                pickups[i] -= (cap - pick)
                pick = cap
            else:
                pick += pickups[i]
                pickups[i] = 0

            if deli == cap and pick == cap:
                break
        
        if dis < 0:
            break
        
        # print(n)
        # print("visit", dis)
        answer += (dis)*2

    return answer


cap = 4
n = 5
deliveries = [1,0,3,1,10]
pickups = [0,3,0,4,0]
print(solution(cap, n, deliveries, pickups))

###
import math

def solution(cap, n, deliveries, pickups):
    answer = 0

    deli = 0
    pick = 0
    dis = -1
    new_cap = cap
    for i in range(n-1, -1, -1):
        if dis < i and (deliveries[i] > 0 or pickups[i] > 0):
            print("visit", i+1)
            dis = i+1
            answer += dis*2
                
        deli += deliveries[i]
        if deli > new_cap:
            tmp = math.ceil(deliveries[i] / cap)
            print("visit", i+1)
            print(deli, new_cap)
            if (i+1) != dis:
                answer += (i+1) * 2 * tmp
            
            new_cap += cap * tmp
            print(new_cap)
                
        pick += pickups[i]
        if pick > new_cap:
            tmp = math.ceil(pickups[i] / cap)
            print("visit", i+1)
            print(pick, new_cap)
            if (i+1) != dis:
                answer += (i+1) * 2 * tmp
            
            new_cap += cap * tmp
            print(new_cap)

    return answer
###