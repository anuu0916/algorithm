# 1339 단어 수학
n = int(input())
words = {
    'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
    'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
    'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
    'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0
}

for i in range(n):
    word = input()
    length = len(word)
    for j in range(length):
        words[word[j]] += 10 ** (length - j - 1)

sorted_words = sorted(words.items(), key=lambda item: item[1], reverse=True)

result = 0
for i in range(10):
    result += sorted_words[i][1] * (9 - i)

print(result)
