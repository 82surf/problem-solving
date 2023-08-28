# 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N, H = map(int,input().split())
box = [list(map(int, input().split())) for _ in range(N * H)]
visited = [[0] * M for _ in range(N * H)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (N, 0), (-N, 0)]
def ripe(r, c):
    visited[r][c] = 1

    start_r = (r // N) * N
    end_r = start_r + N - 1

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if start_r <= nr <= end_r and 0 <= nc < M and box[nr][nc] == 0:
            box[nr][nc] = 1


def ripe_box():
    answer = 0
    before_cnt_1 = -1
    while True:
        target_arr = []
        cnt_0 = 0
        cnt_1 = 0
        for i in range(N * H):
            for j in range(M):
                if box[i][j] == 0:
                    cnt_0 += 1
                elif box[i][j] == 1:
                    cnt_1 += 1
                    if not visited[i][j]:
                        target_arr.append((i, j))
        if cnt_0 == 0:
            return answer
        elif cnt_1 == before_cnt_1:
            return -1

        for target in target_arr:
            ripe(*target)
        answer += 1
        before_cnt_1 = cnt_1


print(ripe_box())
