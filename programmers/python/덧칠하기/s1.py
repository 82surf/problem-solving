from collections import deque


def solution(n, m, section):
    answer = 0
    q = deque(section)
    while q:
        max_w = q[0] + m - 1
        while q and q[0] <= max_w:
            q.popleft()
        answer += 1
    return answer
