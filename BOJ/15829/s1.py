import sys
sys.stdin = open('input.txt')

L = int(input())
word = list(map(lambda c: ord(c) - 96, list(input())))
r = 31
M = 1234567891

total = 0
for i, w in enumerate(word):
    total += w * (r ** i)
print(total % M)
