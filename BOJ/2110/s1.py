# 이진 탐색, 매개 변수 탐색
# https://scshim.tistory.com/495 참고한 풀이
# 문제를 거꾸로 푼다. 거리가 d일 때 C개의 공유기를 설치할 수 있는지에 대한 결정 문제로 풀이

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, C = map(int, input().split())
houses = sorted([int(input()) for _ in range(N)])


def check(distance):
    cnt = C - 1
    tmp = houses[0]
    for i in range(1, N):
        if tmp + distance <= houses[i]:
            tmp = houses[i]
            cnt -= 1
        if cnt == 0:
            return True
    return False


def binary_search():
    lo, hi = 1, houses[-1] - houses[0]
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    return hi if check(hi) else lo


print(binary_search())
