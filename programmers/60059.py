# 60059 자물쇠와 열쇠

# 2차원 리스트 시계방향 90도 회전
def rotate(a):
    n = len(a) # 행 길이
    m = len(a[0]) # 열 길이
    # 90도 회전 -> n이 열 길이, m이 행 길이가 됨
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result


# 원래 자물쇠 부분(3배 확장한 자물쇠의 가운데 부분)이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock)//3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock) # 자물쇠 크기
    m = len(key) # 열쇠 크기
    
    # 자물쇠 크기 3배 확장
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
    # 새로운 자물쇠 중앙 부분에 기존의 자물쇠 값 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]
    
    # 4가지 회전 방향에 대해 열쇠로 자물쇠를 열 수 있는지 확인
    for rotation in range(4):
        key = rotate(key) # 열쇠 회전
        
        # 왼쪽 위부터 한 칸씩 옮기며 탐색
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠를 자물쇠에 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                
                # 새로운 자물쇠에 열쇠가 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                
                # 자물쇠에서 열쇠 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    
    # 모든 경우에도 열쇠가 자물쇠에 맞지 않는 경우
    return False
