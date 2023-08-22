# 재귀
# 풀이는 가능하나 시간초과

import sys
sys.stdin = open('input.txt')

n, r, c = map(int, input().split())
N = 2 ** n
matrix = [[0] * N for _ in range(N)]
cnt = 0
dirs = [(0, 0), (0, 1), (1, 0), (1, 1)]


def recursive(sr, sc, N):
    global cnt

    if N != 1:
        next_n = N // 2
        next_starts = [(sr, sc), (sr, sc + next_n), (sr + next_n, sc), (sr + next_n, sc + next_n)]
        for nr, nc in next_starts:
            recursive(nr, nc, next_n)
    else:
        matrix[sr][sc] = cnt
        cnt += 1


recursive(0, 0, N)
print(matrix[r][c])