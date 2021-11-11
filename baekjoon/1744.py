# 1744 수 묶기
n = int(input())
p_num = []  # 양수 배열
n_num = []  # 음수 배열
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)
    if num > 0:
        p_num.append(num)
    else:
        n_num.append(num)

sorted_positive_num = sorted(p_num, reverse=True)
sorted_negative_num = sorted(n_num)

result = 0  # 결과값
p_multi = 0  # n>1인 수끼리 곱함
n_multi = 0  # n<0인 수끼리 곱함
zero_cnt = 0  # 0 개수

# 양수 배열 계산
for n in sorted_positive_num:
    # 1 이상이면 무조건 곱하는 게 이득
    if n > 1:
        if p_multi == 0:  # 첫 번째 수 저장
            p_multi = n
        else:
            p_multi *= n  # 두 번째 수 곱함
            result += p_multi  # 결과값에 더해줌
            p_multi = 0  # 한 번 묶었으니 초기화
    elif n == 1:  # 1일 때는 무조건 더하는게 이득
        result += n

# 음수 배열 계산
for n in sorted_negative_num:
    if n == 0:  # 0 개수 카운트
        zero_cnt += 1
    elif n < 0:
        if n_multi == 0:  # 첫 번째 수 저장
            n_multi = n
        else:
            n_multi *= n  # 두 번째 수 곱함
            result += n_multi  # 결과값에 더해줌
            n_multi = 0  # 한 번 묶었으니 초기화

# 남은 수 더함
if p_multi != 0:
    result += p_multi
if n_multi != 0 and zero_cnt == 0:
    result += n_multi

print(result)
