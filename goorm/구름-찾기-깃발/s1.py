import sys
input = sys.stdin.readline

N, K = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(N)]

# 깃발 꽂기 & 찾기
answer = 0
dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for r in range(N):
    for c in range(N):
        if M[r][c] == 0:
            cnt = 0
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and M[nr][nc] == 1:
                    cnt -= 1
            if cnt == -K:
                answer += 1

print(answer)
