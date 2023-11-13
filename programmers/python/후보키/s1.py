from itertools import combinations


def check(relation, columns):
    key_set = set()
    for t in relation:
        key = ""
        for n in columns:
            key += t[n]
        if key in key_set:
            return False
        key_set.add(key)
    return True


def is_valid(a, b):
    set_a, set_b = set(a), set(b)
    intersection = set_a & set_b
    if intersection == set_a or intersection == set_b:
        return False
    return True


def solution(relation):
    N = len(relation[0])
    candidate_key_list = []
    for i in range(1, N + 1):
        for comb in combinations(range(N), i):
            flag = True
            for key in candidate_key_list:
                if not is_valid(comb, key):
                    flag = False
                    break
            if flag and check(relation, comb):
                candidate_key_list.append(comb)
    return len(candidate_key_list)