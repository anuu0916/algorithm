# 1931 회의실 배정
# 참고 : https://suri78.tistory.com/26
import sys
input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 일찍 끝나는 순서대로 정렬
arr.sort(key = lambda x: (x[1], x[0]))

i = 1
end = arr[0][1]
cnt = 1

for i in range(1, n):
    # 뒷 순서 회의와 겹치지 않으면 +1
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]

print(cnt)
