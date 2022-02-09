# 60063 블록 이동하기
from collections import deque

# 상하좌우 이동
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

# 로봇이 가로로 있을 때 90도 회전
# 시계방향 아래로 회전, 반시계방향 아래로 회전 순서
hdx = [1, 1]
hdy = [-1, 1]

# 로봇이 세로로 있을 때 90도 회전
# 시계방향 아래로 회전, 반시계방향 아래로 회전 순서
vdx = [1, 1]
vdy = [1, -1]

def solution(board):
    n = len(board)
    queue = deque([[(0,0), (0,1), 0]])  # 왼쪽 좌표, 오른쪽 좌표, 걸린 시간

    while queue:
        left, right, t = queue.popleft()
        if left == (n-1, n-1) or right == (n-1, n-1):
            return t
        
        # 상하좌우 이동
        for _ in range(4):
            L_nextX, L_nextY = left[0] + dx[_], left[1] + dy[_]
            R_nextX, R_nextY = right[0] + dx[_], right[1] + dy[_]

            # 인덱스가 배열 범위 내인지 검사
            if 0 <= L_nextX < n and 0 <= L_nextY < n:
                if 0 <= R_nextX < n and 0 <= R_nextY < n:
                    # 이동한 칸에 벽이 없는지 검사
                    if board[L_nextX][L_nextY] == 0 and board[R_nextX][R_nextY] == 0:
                        queue.append([(L_nextX, L_nextY), (R_nextX, R_nextY), t+1])
        
        # 90도 회전
        if left[0] == right[0] :  # 로봇이 가로로 있을 때
            for i in range(2):

        

    return answer


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))