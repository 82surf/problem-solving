from math import inf
import sys
sys.stdin = open('input.txt')

# 입력받기
N, M = map(int, input().split())
board = [input() for _ in range(N)]

# 체스보드 만들기
white_line = 'WB' * 4
black_line = 'BW' * 4
white_board = [white_line, black_line] * 4
black_board = [black_line, white_line] * 4

# 완전탐색
answer = inf
for i in range(N - 7):
    for j in range(M - 7):
        w_cnt, b_cnt = 0, 0
        for r in range(8):
            for c in range(8):
                nr, nc = i + r, j + c
                if board[nr][nc] != white_board[r][c]:
                    w_cnt += 1
                if board[nr][nc] != black_board[r][c]:
                    b_cnt += 1
        if answer > w_cnt:
            answer = w_cnt
        if answer > b_cnt:
            answer = b_cnt

print(answer)