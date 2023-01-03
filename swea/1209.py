# Sum
import sys
input = sys.stdin.readline

for test_case in range(1, 11):
    case_num = int(input())
    arr = []
    answer = 0

    for i in range(100):
        tmp = list(map(int, input().split()))
        answer = max(sum(tmp), answer)
        arr.append(tmp)
    
    arr_col = list(zip(*arr[::-1]))
    for i in range(100):
        answer = max(sum(arr_col[i]), answer)
    
    dia1 = 0
    dia2 = 0
    for i in range(100):
        dia1 += arr[i][i]
        dia2 += arr[i][99-i]
    
    answer = max(dia1, dia2, answer)

    print("#%d %d" % (case_num, answer))
