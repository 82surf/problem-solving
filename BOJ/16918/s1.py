import sys
sys.stdin = open('input.txt')

R, C, N = map(int, input().split())


def init_string(s):
    result = [0] * len(s)
    for i, c in enumerate(s):
        result[i] = 0 if c == '.' else 4
    return result


def boom(i, j):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dr, dc in dirs:
        nr, nc = i + dr, j + dc
        if 0 <= nr < R and 0 <= nc < C:
            if matrix[nr][nc] != 1:
                matrix[nr][nc] = 0
    matrix[i][j] = 0


def print_answer(m):
    result = [['.' for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if m[i][j]:
                result[i][j] = 'O'
    for r in result:
        print(''.join(r))


matrix = [init_string(input()) for _ in range(R)]

for t in range(1, N + 1):
    # 1초 감소
    for i in range(R):
        for j in range(C):
            if matrix[i][j]:
                matrix[i][j] -= 1
    # 홀수 초: 폭발
    if t % 2:
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 1:
                    boom(i, j)
    # 짝수 초: 설치
    else:
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    matrix[i][j] = 4

print_answer(matrix)
