# 최빈수 구하기
T = int(input())
answer = []

for test_case in range(1, T+1):
    score = [[i, 0] for i in range(101)]

    case_num = int(input())
    arr = list(map(int, input().split()))

    for a in arr:
        score[a][1] += 1
    
    score.sort(key= lambda x : (-x[1], -x[0]))

    answer.append("#%d %d" % (test_case, score[0][0]))

for ans in answer:
    print(ans)
