# BFS로 풀이 시도
# 시간 복잡도 너무 커짐 + BFS 종료 조건이 없음

from collections import deque
from itertools import combinations


def pop_n_push(q1, q2):
    rq1, rq2 = q1.copy(), q2.copy()
    rq2.append(rq1.popleft())
    return rq1, rq2


def bfs(q1, q2):
    q = deque([(q1.copy(), q2.copy(), 0)])
    while q:
        nq1, nq2, cnt = q.popleft()

        next1 = pop_n_push(nq1, nq2)
        if sum(next1[0]) == sum(next1[1]):
            return cnt + 1

        next2 = pop_n_push(nq2, nq1)
        if sum(next2[0]) == sum(next2[1]):
            return cnt + 1

        q.append([next1[0], next1[1], cnt + 1])
        q.append([next2[0], next2[1], cnt + 1])


def solution(queue1, queue2):
    # 두 큐의 합이 같을 수 있다면 BFS
    nums = queue1 + queue2
    half = sum(nums) // 2
    q1, q2 = deque(queue1), deque(queue2)
    for c in combinations(nums, len(queue1)):
        if sum(c) == half:
            return bfs(q1, q2)
    else:
        return -1
    return answer