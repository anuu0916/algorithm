# 1764 듣보잡
n, m = map(int, input().split())
heard = []  # 듣도 못한 사람
saw = []  # 보도 못한 사람
hs = []  # 듣보잡

for i in range(n):
    heard.append(input())

for i in range(m):
    saw.append(input())

hs = list(set(heard) & set(saw))

print(len(hs))
hs.sort()
for n in hs:
    print(n)
