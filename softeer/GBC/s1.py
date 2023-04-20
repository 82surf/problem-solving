# 통과 코드
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
while True:
    if log_velo - limit_velo > answer:
        answer = log_velo - limit_velo

    if limit_dist > log_dist:
        limit_dist -= log_dist
        log_idx += 1
        if log_idx < len(log):
            log_dist, log_velo = log[log_idx]
    elif limit_dist == log_dist:
        limit_idx += 1
        log_idx += 1
        if log_idx < len(log):
            log_dist, log_velo = log[log_idx]
        if limit_idx < len(limit):
            limit_dist, limit_velo = limit[limit_idx]
    else:
        log_dist -= limit_dist
        limit_idx += 1
        if limit_idx < len(limit):
            limit_dist, limit_velo = limit[limit_idx]

    if limit_idx == len(limit) and log_idx == len(log):
        break

print(answer)

