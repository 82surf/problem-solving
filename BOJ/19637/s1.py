# N * M은 최악의 경우 100억회의 연산
# 단순 if문이 아닌 이분탐색으로 풀이

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 칭호 입력받기
N, M = map(int, input().split())
title_names = [0] * N
title_vals = [0] * N
for i in range(N):
    title_name, title_val = input().split()
    title_names[i] = title_name
    title_vals[i] = int(title_val)


# 이분탐색 결정 함수
def check(idx, val):
    return val <= title_vals[idx]


# 각 숫자 별 이분탐색 수행
for _ in range(M):
    val = int(input())
    lo, hi = 0, N-1
    while lo+1 < hi:
        mid = (lo + hi) // 2
        if check(mid, val):
            hi = mid
        else:
            lo = mid

    if check(lo, val):
        print(title_names[lo])
    else:
        print(title_names[hi])