# 9935 문자열 폭발
import sys
input = sys.stdin.readline
sentence = input().rstrip()
bomb = input().rstrip()
blen = len(bomb)
stack = []

for s in sentence:
    stack.append(s)
    if s == bomb[-1] and ''.join(stack[-blen:]) == bomb:
        del stack[-blen:]

answer = ''.join(stack)

if len(answer) == 0:
    print("FRULA")
else:
    print(answer)
