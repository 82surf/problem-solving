# 시간초과
from itertools import combinations, product

def solution(weights):
    answer = 0
    # weights에서 2개를 고르는 조합 생성하기
    for w in combinations(weights, 2):
        # [2, 3, 4]에서 2개를 고르는 중복 조합 생성하기
        for m in product([2, 3, 4], repeat=2):
            if w[0] * m[0] == w[1] * m[1]:
                answer += 1
                break
    return answer