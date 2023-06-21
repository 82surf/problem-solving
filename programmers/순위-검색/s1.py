# TC 통과
# 시간초과

# query 10만
# 최대 50만
# 최대 200만

# info 배열의 원소 객체로 변환
# query 배열의 원소 객체로 변환

# query 배열을 순회하면서 검색 수행


def refine(string, seperator):
    result = string
    if seperator:
        result = result.replace(seperator, ' ')
    result = result.split()
    result[-1] = int(result[-1])
    return result


def check(info, query):
    if info[-1] < query[-1]:
        return False

    for i in range(4):
        if query[i] != '-' and info[i] != query[i]:
            return False

    return True


def solution(info, query):
    info_refined = list(map(lambda x: refine(x, None), info))
    query_refined = list(map(lambda x: refine(x, ' and '), query))

    answer = [0] * len(query_refined)
    for idx, q in enumerate(query_refined):
        cnt = 0
        for i in info_refined:
            if check(i, q):
                cnt += 1
        answer[idx] = cnt

    return answer