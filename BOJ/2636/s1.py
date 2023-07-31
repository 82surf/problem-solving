from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def main():
    R, C = map(int, input().split())
    plate = [list(map(int, input().split())) for _ in range(R)]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cheese_cnt = 0

    def count_cheese():
        nonlocal cheese_cnt
        for r in range(R):
            for c in range(C):
                if plate[r][c]:
                    cheese_cnt += 1

    def BFS():
        q = deque([(0, 0)])
        visited = [[0] * C for _ in range(R)]
        visited[0][0] = 1
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] and plate[nr][nc] != 2:
                    if plate[nr][nc] == 1:
                        plate[nr][nc] = 2
                    else:
                        q.append((nr, nc))
                    visited[nr][nc] = 1

    def melt():
        melt_count = 0
        for r in range(R):
            for c in range(C):
                if plate[r][c] == 2:
                    melt_count += 1
                    plate[r][c] = 0
        return melt_count

    def solution():
        nonlocal cheese_cnt
        count_cheese()
        cycle_cnt = 0
        melt_count = 0
        while cheese_cnt:
            cycle_cnt += 1
            BFS()
            melt_count = melt()
            cheese_cnt -= melt_count
        print(cycle_cnt)
        print(melt_count)

    solution()


main()
