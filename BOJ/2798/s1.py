import sys
sys.stdin = open('input.txt')
from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
for c in combinations(cards, 3):
    total = sum(c)
    if total <= M and answer < total:
        answer = total

print(answer)