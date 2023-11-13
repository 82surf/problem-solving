# 시간초과

import sys
sys.setrecursionlimit(1000000)


def solution(x, y, n):
    answer = 1000001

    def calc(s, cnt):
        nonlocal answer

        if s > y or cnt >= answer:
            return
        elif s == y and answer >= cnt:
            answer = cnt
            return

        calc(s + n, cnt + 1)
        calc(s * 2, cnt + 1)
        calc(s * 3, cnt + 1)

    calc(x, 0)

    return answer if answer != 1000001 else -1