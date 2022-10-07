# 5648 원자 소멸 시뮬레이션
# 시간초과 뜸....

from collections import deque
board = [[0] * 4001 for _ in range(4001)]
queue = deque()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
	
    result = 0
    # 배열 좌표는 (y, x)
    for i in range(n):
        x, y, d, k = map(int, input().split())
        x = (x+1000) * 2
        y = (y+1000) * 2
        board[y][x] = 1
        queue.append([x, y, d, k])

    if n < 2:
        break

    while len(queue) > 1:
        # 원자 이동
        for i in range(len(queue)):
            x, y, d, k = queue.popleft()
            board[y][x] -= 1
            # print(x, y, d, k)
            if d == 0: # 상
                y += 1
            elif d == 1: # 하
                y -= 1
            elif d == 2: # 좌
                x -= 1
            elif d == 3: # 우
                x += 1
            
            if 0 <= x <= 4000 and 0 <= y <= 4000:
                board[y][x] += 1
                queue.append([x, y, d, k])
        
        # 충돌 확인
        # print(queue)
        for i in range(len(queue)):
            if len(queue) == 0:
                break
            x, y, d, k = queue.popleft()
            
            if board[y][x] > 1:
                # print("(%d, %d), k=%d"%(x, y, k), end = ", ")
                tmp = k
                board[y][x] = 0
                for j in range(len(queue)):
                    if len(queue) == 0:
                        break

                    qx, qy, qd, qk = queue.popleft()
                    if x == qx and y == qy:
                        # print("(%d, %d), k=%d"%(qx, qy, qk), end = ", ")
                        tmp += qk
                    else:
                        queue.append([qx, qy, qd, qk])
                result += tmp
                # print("충돌", tmp)
            else:
                queue.append([x, y, d, k])
        # print(result)
    
    # board 초기화
    for i in range(len(queue)):
        x, y, d, k = queue.pop()
        board[y][x] = 0
    
    print("#%d %d"%(test_case, result))