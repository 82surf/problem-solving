import math


def get_multiset(s):
    multiset = {'total': 0}
    for i in range(len(s) - 1):
        e = s[i] + s[i + 1]
        if e.isalpha():
            if e in multiset:
                multiset[e] += 1
            else:
                multiset[e] = 1
            multiset['total'] += 1
    return multiset


def solution(str1, str2):
    ms1, ms2 = get_multiset(str1.upper()), get_multiset(str2.upper())  # 중복집합 생성
    intersection, union = 0, 0  # 교집합, 차집합의 원소 개수

    for e1 in ms1:  # 교집합 원소의 개수 구하기
        if e1 == 'total':
            continue
        e1_cnt = ms1[e1]
        if e1 in ms2:
            e2_cnt = ms2[e1]
            intersection += e1_cnt if e1_cnt < e2_cnt else e2_cnt

    union = ms1['total'] + ms2['total'] - intersection  # 합집합 원소의 개수

    return math.trunc(intersection / union * 65536) if union else 65536