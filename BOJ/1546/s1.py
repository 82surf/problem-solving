import sys
sys.stdin = open('input.txt')

N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

total = 0
for score in scores:
    total += score / M * 100
print(total / N)