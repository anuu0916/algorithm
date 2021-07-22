# 7562 나이트의 이동
import sys
from collections import deque
moves = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
test_case = int(input())

# 원래는 이 3개 값을 맨 아래 for문에서 받았는데
# 그러니까 값을 다 입력하기도 전에 앞 테스트케이스들의 결과가 출력돼서 따로 받았습니다
i = deque()
start = deque()
end = deque()
for _ in range(test_case):
    i.append(int(input()))
    start.append(list(map(int, sys.stdin.readline().split())))
    end.append(list(map(int, sys.stdin.readline().split())))


# 인접리스트(딕셔너리), 최소경로 저장(딕셔너리), 방문검사(배열)로 해서
# 경우의 수가 많으니까 큐에 값을 넣을 때만 인접리스트를 갱신하고
# not in list 혹은 not in keys()로 검사했더니 오래걸리더라고요... 매번 배열 길이 O(N)만큼 걸림
# 매번 인접리스트를 만드는 것도 시간이 오래 걸리더라고요
# 그래서 구글링해서 참고했습니다...
# visited를 아예 IxI 크기만큼 미리 만들어놓고 검사하는게 not in보다 빨랐어요
# 인접리스트도 따로 안만들고 그때그때 큐에 바로 넣었습니다
# 그때그때 인접리스트 만들 생각은 했으면서 왜 큐에 바로 넣을 생각은 안했지...?
# 최소 step 구하는것도 따로 딕셔너리 만들지 않고 큐에 바로 넣었어요
# (x, y, step) 이런 식으로 큐에 넣어 구현했습니다

for cnt in range(test_case):
    x = start[cnt][0]
    y = start[cnt][1]
    dstX = end[cnt][0]
    dstY = end[cnt][1]

    queue = deque()
    queue.append((x, y, 0))
    visited = [[0 for _ in range(i[cnt])] for _ in range(i[cnt])]

    while len(queue) > 0:
        top = queue.popleft()

        # 목적지에 도착하면 step 프린트 후 break
        if top[0] == dstX and top[1] == dstY:
            print(top[2])
            break

        # 방문한 노드가 아닐 경우
        if visited[top[0]][top[1]] == 0:
            visited[top[0]][top[1]] = 1

            # 나이트 이동 경로를 통해 인접노드 큐에 넣음
            for move in moves:
                nextX = top[0] + move[0]
                nextY = top[1] + move[1]
                if nextX >= 0 and nextX < i[cnt] and nextY >= 0 and nextY < i[cnt]:
                    queue.append((nextX, nextY, top[2]+1))

