# 제출 결과: TC 통과, 일부 시간 초과

from collections import deque


def BFS(start, end, maps, H, W):
    visited = [[0] * W for _ in range(H)]
    visited[start[0]][start[1]] = 1
    q = deque([(start[0], start[1], 0)])

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        r, c, cnt = q.popleft()
        if (r, c) == end:
            return cnt
        visited[r][c] = 1

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] != 'X' and not visited[nr][nc]:
                q.append((nr, nc, cnt + 1))
    return -1


def search(maps, H, W):
    S, E, L = None, None, None
    for i in range(H):
        for j in range(W):
            if maps[i][j] == 'S':
                S = (i, j)
            elif maps[i][j] == 'E':
                E = (i, j)
            elif maps[i][j] == 'L':
                L = (i, j)
    return S, E, L


def solution(maps):
    H, W = len(maps), len(maps[0])
    S, E, L = search(maps, H, W)

    lever_cnt = BFS(S, L, maps, H, W)
    if lever_cnt < 0:
        return -1

    end_cnt = BFS(L, E, maps, H, W)
    if end_cnt < 0:
        return -1

    return lever_cnt + end_cnt