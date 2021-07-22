# 1475 방 번호
import math

# 문자열로 입력받음
number = input()
# 각 숫자의 중복 개수를 저장할 딕셔너리
count = {}

# 반복문을 돌며 count로 중복 검사
for i in number:
    count[i] = number.count(i)

    # 중복을 다 찾았을 경우 break
    values = count.values()
    if sum(values) == len(number):
        break

# 6, 9 중복 계산을 위해 하나씩 만들어줍니다...
if '6' not in count:
    count['6'] = 0
if '9' not in count:
    count['9'] = 0

# 9 중복 개수를 6으로 합친 다음, 2로 나눈 천장수를 구한다
# 2로 나눈 천장수 = 6과 9를 만들 수 있는 세트 개수
count['6'] += count['9']
del (count['9'])
count['6'] = math.ceil(count['6'] / 2)

# 서로 대체할 수 없는 숫자들끼리만 딕셔너리에 남아있으므로
# 중복 수의 최댓값이 세트 개수이다
values = count.values()
print(max(values))
