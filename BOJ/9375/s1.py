# 시간초과

from itertools import combinations
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    closet = {}
    for _ in range(n):
        item, category = input().split()
        if category in closet:
            closet[category].append(item)
        else:
            closet[category] = [item]

    answer = 0
    for i in range(1, len(closet) + 1):
        for categories in combinations(closet.keys(), i):
            cases = 1
            for category in categories:
                cases *= len(closet[category])
            answer += cases
    print(answer)