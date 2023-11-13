from collections import deque


def solution(board):
    R, C = len(board), len(board[0])

    def search_start():
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'R':
                    return r, c

    def is_opposite(dir1, dir2):
        if dir1 and dir2:
            r1, c1 = dir1
            r2, c2 = dir2

            return (r1 == r2 == 0 and c1 == -c2) or (r1 == -r2 and c1 == c2 == 0)
        return False

    def slide(start, direction):
        r, c = start
        dr, dc = direction

        while 0 <= r < R and 0 <= c < C and board[r][c] != 'D':
            r += dr
            c += dc

        return r - dr, c - dc

    def BFS(start):
        sr, sc = start
        q = deque([((sr, sc), 0, None)])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[0] * C for _ in range(R)]
        visited[sr][sc] = 1

        while q:
            node, cnt, dir_before = q.popleft()
            r, c = node
            if board[r][c] == 'G':
                return cnt

            for direction in dirs:
                if not is_opposite(direction, dir_before):
                    next_node = slide(node, direction)
                    nr, nc = next_node
                    if next_node != node and not visited[nr][nc]:
                        q.append((next_node, cnt + 1, direction))
                        visited[nr][nc] = 1
        return -1

    return BFS(search_start())

