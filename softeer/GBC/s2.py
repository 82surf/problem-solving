# 리팩토링

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
limit = [list(map(int, input().split())) for _ in range(N)]
log = [list(map(int, input().split())) for _ in range(M)]

limit_idx, log_idx = 0, 0
limit_dist, limit_velo = limit[limit_idx]
log_dist, log_velo = log[log_idx]

answer = 0


def next_log():
    global log_idx, log_dist, log_velo
    log_idx += 1
    if log_idx < len(log):
        log_dist, log_velo = log[log_idx]


def next_limit():
    global limit_idx, limit_dist, limit_velo
    limit_idx += 1
    if limit_idx < len(limit):
        limit_dist, limit_velo = limit[limit_idx]


while True:
    if log_velo - limit_velo > answer:
        answer = log_velo - limit_velo

    if limit_dist > log_dist:
        limit_dist -= log_dist
        next_log()
    elif limit_dist == log_dist:
        next_limit()
        next_log()
    else:
        log_dist -= limit_dist
        next_limit()

    if limit_idx == len(limit) and log_idx == len(log):
        break

print(answer)

