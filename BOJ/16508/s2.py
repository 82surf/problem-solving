from math import inf
from itertools import combinations
import sys
sys.stdin = open('input.txt')


def convert(s):
    arr = s.split()
    arr[0] = int(arr[0])
    arr[1] = str_to_dic(arr[1])
    return arr


def str_to_dic(s):
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    return dic


def add_dic(dic_a, dic_b):
    for key, val in dic_b.items():
        if key in dic_a:
            dic_a[key] += val
        else:
            dic_a[key] = val
    return dic_a


def check(target_dic, book_dic):
    for key, val in target_dic.items():
        if key not in book_dic or book_dic[key] < val:
            return False
    return True


T = str_to_dic(input())
N = int(input())
books = [convert(input()) for _ in range(N)]
answer = inf

for i in range(1, N+1):
    for comb in combinations(range(N), i):
        book_dic = {}
        price = 0
        for idx in comb:
            add_dic(book_dic, books[idx][1])
            price += books[idx][0]

        if check(T, book_dic) and answer > price:
            answer = price

print(answer if answer != inf else -1)
