# 1918 후위 표기식
import sys
from collections import deque

expr = list(sys.stdin.readline())
expr = expr[:-1]
stack = deque([])
op = ["+", "-", "*", "/", "(", ")"]
result = ""

for i in range(len(expr)):
    cur = expr[i]
    if cur in op:
        if not stack:
            stack.append(cur)
        elif cur == "(":
            stack.append(cur)
        elif cur == ")":
            while True:
                top = stack.pop()
                if top == "(":
                    break
                else:
                    result += top
        elif cur == '*' or cur == '/':
            while stack:
                top = stack[-1]
                if top == '*' or top == '/':
                    result += stack.pop()
                else:
                    break
            stack.append(cur)
        elif cur == '-' or cur == '+':
            while stack:
                top = stack[-1]
                if top == '(':
                    break
                else:
                    result += stack.pop()
            stack.append(cur)
    else:
        result += cur

for i in range(len(stack)):
    result += stack.pop()

print(result)
