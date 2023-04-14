"""
테스트케이스 통과, 시간초과
"""

# 정사각형을 만들 수 있는 시작 좌표 이터레이터를 반환하는 함수
# 단, n은 r, c보다 작다
def squares(r, c, n):
    for i in range(r - n + 1):
        for j in range(c - n + 1):
            yield i, j


# 0인 좌표 배열을 반환하는 함수
def get_zeros(board, r, c):
    zero = []
    for i in range(r):
        for j in range(c):
            if not board[i][j]:
                zero.append((i, j))
    return zero


# 정사각형 시작점과 0 좌표 배열을 가지고 정사각형이 되는지 검증하는 함수
def is_valid(sr, sc, n, zeros):
    for zr, zc in zeros:
        if sr <= zr < sr + n and sc <= zc < sc + n:
            return False
    return True


def solution(board):
    r, c = len(board), len(board[0])            # 보드 행, 열 길이
    zeros = get_zeros(board, r, c)              # 0 좌표 배열 캐싱
    max_n = min(r, c)                           # 정사각형을 만들 수 있는 최대 길이

    for n in range(max_n, -1, -1):              # 정사각형 길이를 1씩 줄이면서
        for sr, sc in squares(r, c, n):         # 가능한 정사각형 좌표마다
            if is_valid(sr, sc, n, zeros):      # 0이 들어가는지 확인
                return n ** 2                   # 정사각형 되면 정답 반환
