from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs():
    visited = [[0] * M for _ in range(N)]
    q = deque([(0, 0, 1)])
    while q:
        n, m, cnt = q.popleft()
        if n == N - 1 and m == M - 1:
            return cnt
        for d in dirs:
            next_n, next_m = n + d[0], m + d[1]
            if 0 <= next_n < N and 0 <= next_m < M:
                if maze[next_n][next_m] and not visited[next_n][next_m]:
                    q.append((next_n, next_m, cnt + 1))
                    visited[next_n][next_m] = 1


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print(bfs())
