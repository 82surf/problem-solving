import sys, re
from collections import deque
sys.stdin = open('input.txt')


def solution():
    board = input()
    x_arr = re.split("\.+", board)
    dot_arr = re.split("X+", board)
    # print(x_arr, dot_arr)

    for i, x in enumerate(x_arr):
        n = len(x)
        if n % 2:
            return -1
        elif n == 2:
            x_arr[i] = 'BB'
        elif n > 2:
            A_cnt = n // 4
            B_cnt = (n - A_cnt * 4) // 2
            x_arr[i] = 'AAAA' * A_cnt + 'BB' * B_cnt

    answer = ''
    xq, dq = deque(x_arr), deque(dot_arr)
    if xq[0] == '':
        while xq and dq:
            answer += xq.popleft() + dq.popleft()
    else:
        while xq and dq:
            answer += dq.popleft() + xq.popleft()
    return answer


print(solution())