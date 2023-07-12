import sys
sys.stdin = open('input.txt')

K, N = map(int, input().split())
items = [int(input()) for _ in range(K)]


def check(n):
    cnt = 0
    for item in items:
        cnt += item // n
    return cnt >= N


lo, hi = 1, max(items)
if check(lo) != check(hi):
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)
else:
    print(hi)