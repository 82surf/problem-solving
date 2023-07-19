from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    docs = list(map(int, input().split()))

    tmp_q = [0] * len(docs)
    for idx, priority in enumerate(docs):
        tmp_q[idx] = (idx, priority)
    q = deque(tmp_q)

    def print_available():
        for i in range(1, len(q)):
            if q[i][1] > q[0][1]:
                return False
        return True

    def solution():
        cnt = 0
        while True:
            if print_available():
                cnt += 1
                idx, priority = q.popleft()
                if idx == M:
                    return cnt
            else:
                q.append(q.popleft())

    print(solution())