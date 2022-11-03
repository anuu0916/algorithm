# 12904 A와 B
from collections import deque
s = input().rstrip()
t = input().rstrip()
check = 0

while len(t) >= len(s):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]
    
    if t == s:
        check = 1
        break

print(check)
