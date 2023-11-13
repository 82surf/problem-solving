# DP
def solution(board):
    answer = 1 if board[0][0] else 0
    r, c = len(board), len(board[0])
    for i in range(1, r):
        for j in range(1, c):
            if board[i][j]:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
            if answer < board[i][j]:
                answer = board[i][j]
    return answer ** 2