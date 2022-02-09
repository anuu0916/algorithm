# 60058 괄호 변환
from collections import deque

def divide(p):
    left = 0
    right = 0
    
    for i in range(len(p)):
        if p[i] == "(":
            left += 1
        if p[i] == ")":
            right += 1
        
        if left == right:
            u = p[:i + 1]
            v = p[i + 1 :]
            return u, v


def check_right_string(u):
    stack = deque()
    
    for i in range(len(u)):
        stack.append(u[i])
        if len(stack) >= 2:
            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()
    
    if len(stack) > 0:
        return False
    else:
        return True


def reverse(u):
    for i in range(len(u)):
        if u[i] == "(":
            u[i] = ")"
        else:
            u[i] = "("
    return u

def solution(p):
    answer=""
    if len(p) == 0:
        return ""
    
    u, v = divide(p)

    if check_right_string(u):
        answer += u
        v = solution(v)
        return u+v
    else:
        tmp = "(" + solution(v) + ")"
        u = reverse(list(u[1:-1]))
        return tmp+"".join(u)


print(solution(")("))
