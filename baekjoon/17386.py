# 17386 선분 교차 1
# ccw 설명 참고 : https://degurii.tistory.com/47
# 코드 설명 참고 : https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-17386%EB%B2%88-%EC%84%A0%EB%B6%84-%EA%B5%90%EC%B0%A8-1-Java-Python

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A, B, C, D = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])

if ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0:
    print(1)
else:
    print(0)
