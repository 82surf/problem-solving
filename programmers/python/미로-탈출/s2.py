# 제출 결과: TC 통과, 시간초과

from collections import deque


def BFS(start, maps, H, W):
    # 0: 레버 당기기 전 방문 여부
    # 1: 레버 당긴 후 방문 여부
    visited = [[[0, 0] for _ in range(W)] for _ in range(H)]
    # 레버 당기기 전 시작 지점 방문 처리
    visited[start[0]][start[1]][0] = 1
    # r, c, 레버 방문 여부, 이동 횟수
    q = deque([(start[0], start[1], 0, 0)])
    # 탐색할 4방향
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while q:
        r, c, opened, cnt = q.popleft()
        visited[r][c][opened] = 1

        if maps[r][c] == 'L':
            visited[r][c][1] = 1
            opened = 1

        if opened == 1 and maps[r][c] == 'E':
            return cnt

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and maps[nr][nc] != 'X' and not visited[nr][nc][opened]:
                q.append((nr, nc, opened, cnt + 1))

    return -1


def solution(maps):
    H, W = len(maps), len(maps[0])
    for i in range(H):
        for j in range(W):
            if maps[i][j] == 'S':
                return BFS((i, j), maps, H, W)

    return BFS(S, maps, H, W)