from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N, H = map(int,input().split())
box = [list(map(int, input().split())) for _ in range(N * H)]


def BFS(tomatoes):
    # 큐 초기화
    q = deque(tomatoes)

    # 탐색
    max_d = 0
    DIRS_HORIZONTAL = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    DIRS_VERTICAL = [(N, 0), (-N, 0)]
    while q:
        r, c, d = q.popleft()

        if max_d < d:
            max_d = d

        for dr, dc in DIRS_HORIZONTAL:
            nr, nc = r + dr, c + dc

            start_r = (r // N) * N
            end_r = start_r + N - 1

            if start_r <= nr <= end_r and 0 <= nc < M and box[nr][nc] == 0:
                box[nr][nc] = 1
                q.append((nr, nc, d + 1))

        for dr, dc in DIRS_VERTICAL:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N * H and 0 <= nc < M and box[nr][nc] == 0:
                box[nr][nc] = 1
                q.append((nr, nc, d + 1))

    return max_d


def solution():
    riped_tomatoes = []
    for i in range(N * H):
        for j in range(M):
            if box[i][j] == 1:
                riped_tomatoes.append((i, j, 0))

    answer = BFS(riped_tomatoes)

    for i in range(N * H):
        for j in range(M):
            if box[i][j] == 0:
                return -1
    return answer


print(solution())
