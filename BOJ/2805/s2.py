import sys
input = sys.stdin.readline


def check(x, target):
    total = 0
    for tree in trees:
        if tree > x:
            total += tree - x
    return total >= target


N, M = map(int, input().split())
trees = list(map(int, input().split()))

lo, hi = 0, max(trees)
while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(lo, M) == check(mid, M):
        lo = mid
    else:
        hi = mid

print(lo)
