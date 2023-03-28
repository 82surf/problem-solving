# TC 통과, 효율성 체크 모두 실패

from itertools import permutations

def solution(n, k):
    for i, p in enumerate(permutations(range(1, n+1), n)):
        if i+1 == k:
            return list(p)