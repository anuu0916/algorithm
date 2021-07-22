# 1213 팰린드롬 만들기
name = input()
count = {}
values = []

# ----- 입력조건 (생략가능) ----
if len(name) > 50:
    exit()
name = name.upper()
# ----------------------------

# 알파벳 중복 검사
for i in name:
    count[i] = name.count(i)
    values = count.values()
    if sum(values) == len(name):
        break

# 홀수 개수인 알파벳 개수 세기
odd = 0
# 홀수 개수인 알파벳 저장
oddVal = str

for key in count:
    if count[key] % 2 == 1:
        odd += 1
        oddVal = key

# 홀수 개수인 알파벳이 2개 이상이면 팰린드롬 생성 X
if odd > 1:
    print("I'm Sorry Hansoo")
    exit()
elif odd == 1:
    # 홀수개인 알파벳 자리는 가운데로 정해져 있으므로 count 1 감소
    count[oddVal] -= 1

# key들을 알파벳순으로 정렬
keys = list(count.keys())
keys.sort()
# 팰린드롬 처음 절반을 저장할 배열
half = []

# 알파벳 순으로 출력, half 배열에 저장
for i in keys:
    for j in range(int(count[i] / 2)):
        print(i, end="")
        half.append(i)

# 홀수개인 알파벳이 있을 경우 가운데에 출력
if odd == 1:
    print(oddVal, end="")

# 나머지 절반을 거꾸로 출력
for i in range(len(half) - 1, -1, -1):
    print(half[i], end="")
