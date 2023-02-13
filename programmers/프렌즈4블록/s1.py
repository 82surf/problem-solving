def solution(m, n, board):
    # 보드 2차원 배열로 변경
    board = list(map(list, board))

    # 보드 출력
    def prnt():
        for i in range(m):
            print(board[i])
        print()

    # 2x2 블록 찾기
    def search_2x2():
        delta = [(0, 1), (1, 0), (1, 1)]
        coords = []
        for r in range(m - 1):
            for c in range(n - 1):
                if not board[r][c]:
                    continue
                blocks = [(r, c)]
                for d in delta:
                    nr, nc = r + d[0], c + d[1]
                    if board[nr][nc] != board[r][c]:
                        break
                    blocks.append((nr, nc))
                else:
                    coords += blocks
        return coords

    # 블록 터뜨리기
    def bomb():
        nonlocal answer
        for r, c in coords:
            if board[r][c]:
                answer += 1
            board[r][c] = 0

    # 중력 적용하기
    def gravity():
        for c in range(n):
            for r in range(m - 1, -1, -1):
                if not board[r][c]:
                    idx = r
                    while idx > 0 and not board[idx][c]:
                        idx -= 1
                    board[r][c] = board[idx][c]
                    board[idx][c] = 0

    answer = 0  # 터트린 블록 개수
    coords = search_2x2()  # 터트릴 블록 좌표 저장
    while coords:  # 터트릴 블록이 없을 때까지 반복
        bomb()  # 블록을 터트리면서 정답 카운트
        gravity()  # 중력 적용하기
        coords = search_2x2()  # 터트릴 블록 좌표 갱신
    return answer
