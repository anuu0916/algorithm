# 17609 회문
T = int(input())


def pseudo(sentence, front, rear):
    while front < rear:
        if sentence[front] != sentence[rear]:
            return False
        front += 1
        rear -= 1
    return True


def palindrome(sentence, front, rear):
    if sentence == sentence[::-1]:
        return 0
    
    while front < rear:
        if sentence[front] != sentence[rear]:
            check_front = pseudo(sentence, front, rear-1)
            check_rear = pseudo(sentence, front+1, rear)

            if check_front or check_rear:
                return 1
            else:
                return 2
        
        front += 1
        rear -= 1


for _ in range(T):
    sentence = input().strip()
    result = palindrome(sentence, 0, len(sentence)-1)

    print(result)
