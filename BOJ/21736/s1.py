from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
campus = [input() for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def BFS(sr, sc):
    q = deque([(sr, sc)])
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    cnt = 0
    while q:
        r, c = q.popleft()
        if campus[r][c] == 'P':
            cnt += 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and campus[nr][nc] != 'X':
                q.append((nr, nc))
                visited[nr][nc] = 1
    return cnt


def solution():
    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                result = BFS(i, j)
                return result if result else 'TT'


print(solution())