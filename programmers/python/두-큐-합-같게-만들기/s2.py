# 시간초과
# 접근방법
# 두 큐를 합친 후 top과 tail이 연결된 원형이라고 가정
# 인덱스 2개를 골라 자른 뒤 합을 구한다
# 합이 절반과 같으면 최소 이동 횟수 업데이트

from itertools import combinations


def solution(queue1, queue2):
    q = queue1 + queue2
    total = sum(q)
    if total % 2:
        return -1
    half = total // 2
    answer = -1
    for c in combinations(range(len(q)), 2):
        start, end = c
        if sum(q[start:end]) == half:
            cnt = start + end - len(queue1)
            if answer < 0:
                answer = cnt
            elif answer > cnt:
                answer = cnt
    return answer