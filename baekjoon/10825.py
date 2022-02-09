# 10825 국영수
import sys
n = int(input())
student = []

for i in range(n):
    student.append(sys.stdin.readline().split())

'''
x[0]: 이름, x[1]: 국어 점수, x[2]: 영어 점수, x[3]: 수학 점수
1. 국어 점수가 감소하는 순서로
2. 국어 점수가 같으면 영어 점수가 증가하는 순서로
3. 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
4. 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 
5. (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
'''
student.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for s in student:
    print(s[0])