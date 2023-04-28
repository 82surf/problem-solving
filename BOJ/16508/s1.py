# 오답
# 같은 글자가 여러개 있는데 개수가 부족한 경우를 확인할 수 없음

from math import inf
from itertools import combinations
import sys
sys.stdin = open('input.txt')


def convert(s):
    arr = s.split()
    arr[0] = int(arr[0])
    arr[1] = set(list(arr[1]))
    return arr


def check(set_a, set_b):
    return set_a & set_b == set_a


T = set(list(input()))
N = int(input())
books = [convert(input()) for _ in range(N)]

answer = inf
for i in range(1, N + 1):
    for comb in combinations(range(N), i):
        book_set = set()
        for idx in comb:
            book_set |= books[idx][1]

        if check(T, book_set):
            price = 0
            for idx in comb:
                price += books[idx][0]

            if answer > price:
                answer = price

print(answer if answer != inf else -1)
