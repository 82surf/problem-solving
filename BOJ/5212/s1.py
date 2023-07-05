import sys
sys.stdin = open('input.txt')

# 그리드 초기화
R, C = map(int, input().split())
grid = [list(input()) for _ in range(R)]

# 사라질 섬 탐색
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
candidates = []
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'X':
            cnt = 0
            for dr, dc in dirs:
                nr, nc = i + dr, j + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if grid[nr][nc] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt >= 3:
                candidates.append((i, j))

# 섬 삭제
for i, j in candidates:
    grid[i][j] = '.'


# 지도 최대, 최소 범위 탐색
def get_min_r():
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'X':
                return r


def get_min_c():
    for c in range(C):
        for r in range(R):
            if grid[r][c] == 'X':
                return c


def get_max_r():
    for r in range(R-1, -1, -1):
        for c in range(C-1, -1, -1):
            if grid[r][c] == 'X':
                return r


def get_max_c():
    for c in range(C-1, -1, -1):
        for r in range(R-1, -1, -1):
            if grid[r][c] == 'X':
                return c

# 정답 생성 후 출력
answer = []
for r in range(get_min_r(), get_max_r() + 1):
    answer.append(grid[r][get_min_c():get_max_c() + 1])

for a in answer:
    print(''.join(a))