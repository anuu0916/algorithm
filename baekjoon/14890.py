# 14890 경사로
import sys
n, l = map(int, sys.stdin.readline().split())
arr = []
cnt = 0

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 가로 탐색
for a in arr:
    check = 0
    road = [0] * n
    for i in range(1, n):
        if a[i-1] < a[i] :
            if i-l < 0 or a[i] - a[i-1] != 1:
                check += 1
                break
            else:
                base = a[i-1]
                for j in range(1, l+1):
                    if a[i-j] != base or road[i-j] == 1:
                        check += 1
                        # print("pass")
                        break
                if check == 0:
                    for j in range(1, l+1):
                        road[i-j] = 1
        elif a[i-1] > a[i]:
            if i+l-1 >= n or a[i-1] - a[i] != 1:
                check += 1
                # print("pass")
                break
            else:
                base = a[i]
                # print("---", i, "---")
                for j in range(l):
                    # print(i+j)
                    if a[i+j] != base or road[i+j] == 1:
                        check += 1
                        # print("pass")
                        break
                if check == 0:
                    for j in range(l):
                        road[i+j] = 1
        if check > 0:
            break
    if check == 0:
        cnt += 1

# 세로 탐색
for k in range(n):
    check = 0
    # print("line", k)
    road = [0] * n
    for i in range(1, n):
        if arr[i-1][k] < arr[i][k]:
            if i-l < 0 or arr[i][k] - arr[i-1][k] != 1:
                # print("pass 1")
                check += 1
                break
            else:
                base = arr[i-1][k]
                for j in range(1, l+1):
                    if arr[i-j][k] != base or road[i-j] == 1:
                        # print("pass 2")
                        check += 1
                        break
                if check == 0:
                    for j in range(1, l+1):
                        road[i-j] = 1
        elif arr[i-1][k] > arr[i][k]:
            if i+l-1 >= n or arr[i-1][k] - arr[i][k] != 1:
                # print("pass 3")
                check += 1
                break
            else:
                base = arr[i][k]
                # print("----4----", l)
                for j in range(l):
                    # print(i+j)
                    if arr[i+j][k] != base or road[i+j] == 1:
                        # print("pass 4")
                        check += 1
                        break
                if check == 0:
                    for j in range(l):
                        road[i+j] = 1
        
        if check > 0:
            break
    
    if check == 0:
        cnt += 1

print(cnt)