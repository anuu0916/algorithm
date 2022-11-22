# 2477 참외밭
# 참고 : https://itcrowd2016.tistory.com/84
import sys
input = sys.stdin.readline
k = int(input())
rec = []
max_height = 0
max_height_idx = 0
max_width = 0
max_width_idx = 0

for i in range(6):
    dir, dis = map(int, input().split())
    rec.append(dis)

    if dir == 1 or dir == 2:
        if max_width < dis:
            max_width = dis
            max_width_idx = i
    else:
        if max_height < dis:
            max_height = dis
            max_height_idx = i

sub_height = abs(rec[(max_height_idx-1)%6] - rec[(max_height_idx+1)%6])
sub_width = abs(rec[(max_width_idx-1)%6] - rec[(max_width_idx+1)%6])
res = (max_width * max_height - sub_width * sub_height) * k
print(res)
