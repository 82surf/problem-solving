from bisect import bisect_left
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    answer = 0
    for n in A:
        answer += bisect_left(B, n)

    print(answer)