from collections import deque
import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def main():
    R, C = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(R)]
    result = [[-1] * C for _ in range(R)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def start():
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 2:
                    BFS((r, c, 0))

    def BFS(start):
        q = deque([start])
        visited = [[0] * C for _ in range(R)]
        visited[start[0]][start[1]] = 1
        while q:
            r, c, d = q.popleft()
            result[r][c] = d
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and matrix[nr][nc] != 0:
                    q.append((nr, nc, d + 1))
                    visited[nr][nc] = 1

    def search_zero():
        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    result[r][c] = 0

    def print_result():
        for r in result:
            print(*r)

    start()
    search_zero()
    print_result()


main()