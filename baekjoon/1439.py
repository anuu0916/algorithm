# 1439 뒤집기
s = input()

zero = 0  # 0이 연속하는 구간의 개수
one = 0  # 1이 연속하는 구간의 개수

for i in range(len(s) - 1):
    # 0에서 1로 변할 때
    if s[i] == '0' and s[i+1] == '1':
        zero += 1
    # 1에서 0으로 변할 때
    elif s[i] == '1' and s[i+1] == '0':
        one += 1

# 문자열의 마지막에서 구간 카운트 추가
if s[-1] == '0':
    zero += 1
else:
    one += 1

# 더 작은 값만큼 뒤집음
print(min(zero, one))
