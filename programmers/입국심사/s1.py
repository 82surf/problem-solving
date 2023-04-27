def check(n, times, x):
    cnt = 0
    for t in times:
        cnt += x // t
    return cnt >= n


def solution(n, times):
    lo, hi = 0, n * max(times)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if not check(n, times, mid):
            lo = mid
        else:
            hi = mid
    return hi