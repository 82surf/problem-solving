import sys
sys.stdin = open('input.txt')

N = int(input())
word_dic = {}
words = []
for _ in range(N):
    word = input()
    if word not in word_dic:
        word_dic[word] = 1
        words.append(word)

words.sort(key=lambda word: (len(word), word))
for word in words:
    print(word)