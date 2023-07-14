import sys
sys.stdin = open('input.txt')

N = int(input())
req_budgets = list(map(int, input().split()))
M = int(input())

lo, hi, total = 1, 0, 0
for rb in req_budgets:
    total += rb
    if rb > hi:
        hi = rb


def check(n):
    total = 0
    for rb in req_budgets:
        total += rb if rb <= n else n
    return True if total <= M else False


if total <= M:
    print(hi)
else:
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    print(lo)