# RGB 거리
import sys
n = int(input())  # 집의 수
rgb = list()
d = [[0 for _ in range(3)] for _ in range(n)]

# 처음엔 그냥 앞에서부터 최소값을 선택하는 방법을 생각했는데... 안되더라고요
# 2주만에 하려니까 머리 안돌아가서 구글링 했습니다 ㅎㅎ
# https://m.blog.naver.com/occidere/220785383050

for i in range(n):
    rgb.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    if i == 0:
        d[i][0] = rgb[i][0]
        d[i][1] = rgb[i][1]
        d[i][2] = rgb[i][2]
        continue

    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + rgb[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + rgb[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + rgb[i][2]

print(min(d[n-1]))
