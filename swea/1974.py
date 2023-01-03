# 1974 스도쿠 검증
import sys
input = sys.stdin.readline
T = int(input())

for test_case in range(1, T+1):
    sudoku = []
    answer = 1

    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    for i in range(9):
        if sum(sudoku[i]) != 45:
            answer = 0
            break
    
    if answer == 0:
        print("#%d %d" % (test_case, answer))
        continue

    for i in range(9):
        tmp = list(zip(*sudoku))[i]
        if sum(tmp) != 45:
            answer = 0
            break
    
    if answer == 0:
        print("#%d %d" % (test_case, answer))
        continue
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            tmp = [row[j:j+3] for row in sudoku[i:i+3]]
            cnt = sum(tmp[0]) + sum(tmp[1]) + sum(tmp[2])
            if cnt != 45:
                answer = 0
                break
            
    print("#%d %d" % (test_case, answer))
