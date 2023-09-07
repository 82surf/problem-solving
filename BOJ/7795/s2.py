import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def check(flag, val):
    return val >= flag


def binary_search(flag, arr):
    lo, hi = -1, len(arr)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= flag:
            hi = mid
        else:
            lo = mid
    return hi


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    answer = 0
    for n in A:
        answer += binary_search(n, B)
    print(answer)