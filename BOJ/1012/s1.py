import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(20000)
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    visited = [[0] * M for _ in range(N)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def DFS(r, c):
        visited[r][c] = 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and field[nr][nc] and not visited[nr][nc]:
                DFS(nr, nc)

    answer = 0
    for r in range(N):
        for c in range(M):
            if field[r][c] == 1 and not visited[r][c]:
                DFS(r, c)
                answer += 1

    print(answer)
