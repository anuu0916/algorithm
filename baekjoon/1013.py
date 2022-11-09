# 1013 Contact
import re
T = int(input())
p = re.compile('(100+1+|01)+')

for test_case in range(T):
    s = input().rstrip()
    m = p.fullmatch(s)
    if m:
        print("YES")
    else:
        print("NO")
