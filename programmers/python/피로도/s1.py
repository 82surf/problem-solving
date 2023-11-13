from itertools import permutations


def solution(k, dungeons):
    d_len = len(dungeons)
    answer = 0
    for visit_idx in permutations(range(d_len), d_len):
        visit = 0
        temp_k = k
        for i in visit_idx:
            flag, consume = dungeons[i]
            if temp_k >= flag:
                temp_k -= consume
                visit += 1
            if visit == d_len:
                return visit
        if answer < visit:
            answer = visit
    return answer
