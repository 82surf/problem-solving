from itertools import combinations
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    category_dic = {}
    for _ in range(n):
        item, category = input().split()
        if category in category_dic:
            category_dic[category] += 1
        else:
            category_dic[category] = 1

    answer = 1
    for cnt in category_dic.values():
        answer *= (cnt + 1)

    print(answer - 1)