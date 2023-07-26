import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
dots = sorted(list(map(int, input().split())))


def check_start(start, idx):
    return start <= dots[idx]


def check_end(end, idx):
    return dots[idx] <= end


def find_start_idx(start):
    lo, hi = 0, N - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check_start(start, mid):
            hi = mid
        else:
            lo = mid
    return lo if check_start(start, lo) else hi


def find_end_idx(end):
    lo, hi = 0, N - 1
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check_end(end, mid):
            lo = mid
        else:
            hi = mid
    return hi if check_end(end, hi) else lo


for _ in range(M):
    line_start, line_end = map(int, input().split())
    if line_start > dots[-1] or line_end < dots[0]:
        print(0)
    else:
        print(find_end_idx(line_end) - find_start_idx(line_start) + 1)