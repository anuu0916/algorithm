# 17413 단어 뒤집기 2
import sys
input = sys.stdin.readline
sentence = list(input().rstrip())

i = 0
before = 0

while i < len(sentence):
    if sentence[i] == '<':
        i += 1
        while sentence[i] != '>':
            i += 1
        i += 1
    elif sentence[i].isalnum():
        before = i
        while i < len(sentence) and sentence[i].isalnum():
            i += 1
        tmp = sentence[before:i]
        tmp.reverse()
        sentence[before:i] = tmp
    else:
        i += 1

print("".join(sentence))
