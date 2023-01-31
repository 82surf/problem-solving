# 같은 몸무게가 여러명 있다면 시소 짝꿍 쌍을 만들 때 각각 개별적인 쌍으로 만들어야 한다.
# EX) weight: [100, 100, 100]이면 시소 짝꿍은 (100, 100), (100, 100), (100, 100) 3개

from math import comb


def solution(weights):
    answer = 0
    w_cnt = {}

    # weights 개수를 w_cnt dict에 기록
    for w in weights:
        if w in w_cnt:
            w_cnt[w] += 1
        else:
            w_cnt[w] = 1

    # dict를 순회하면서 조건을 만족하는 개수 count
    for w, cnt in w_cnt.items():
        conditions = [w * 3 / 2, w * 2, w * 4 / 3]
        if cnt >= 2:
            answer += comb(cnt, 2)
        for c in conditions:
            if c <= 1000 and c == int(c) and int(c) in w_cnt:
                answer += cnt * w_cnt[int(c)]

    return answer
