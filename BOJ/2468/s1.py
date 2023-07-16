import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)

# 입력받기
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 최고 높이 탐색
max_h = 0
for line in matrix:
    max_tmp = max(line)
    if max_h < max_tmp:
        max_h = max_tmp

# 완전탐색
answer = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for val in range(max_h + 1):
    tmp_matrix = [m[:] for m in matrix] # 지도 복사
    for i in range(N):
        for j in range(N):
            if tmp_matrix[i][j] <= val:
                tmp_matrix[i][j] = -1

    visited = [[0] * N for _ in range(N)] # 방문 여부
    def find(r, c):
        visited[r][c] = 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and tmp_matrix[nr][nc] != -1:
                tmp_matrix[nr][nc] = 0
                find(nr, nc)

    cnt = 0 # 안전영역 개수
    for i in range(N):
        for j in range(N):
            if tmp_matrix[i][j] > 0:
                find(i, j)
                cnt += 1

    if answer < cnt:
        answer = cnt

print(answer)
