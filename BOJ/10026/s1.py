import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N = int(input())
picture = [list(input()) for _ in range(N)]


visited_normal = [[0] * N for _ in range(N)]
DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def normal_person_check(r, c):
    visited_normal[r][c] = 1
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and picture[nr][nc] == picture[r][c] and visited_normal[nr][nc] == 0:
            normal_person_check(nr, nc)


visited_weak = [[0] * N for _ in range(N)]


def rg_weak_person_check(r, c):
    visited_weak[r][c] = 1
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and visited_weak[nr][nc] == 0:
            if picture[r][c] in ['R', 'G'] and picture[nr][nc] in ['R', 'G']:
                rg_weak_person_check(nr, nc)
            elif picture[r][c] == 'B' and picture[nr][nc] == 'B':
                rg_weak_person_check(nr, nc)


normal_person_cnt = 0
rg_weak_person_cnt = 0
for i in range(N):
    for j in range(N):
        if not visited_normal[i][j]:
            normal_person_cnt += 1
            normal_person_check(i, j)
        if not visited_weak[i][j]:
            rg_weak_person_cnt += 1
            rg_weak_person_check(i, j)

print(normal_person_cnt, rg_weak_person_cnt)

