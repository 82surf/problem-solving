from math import inf
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
sys.stdin = open('input.txt')


def dijkstra(N, cave):
    cost = [[inf] * N for _ in range(N)]
    cost[0][0] = cave[0][0]
    # w, r, c
    q = [[cave[0][0], 0, 0]]

    while q:
        w, r, c = heappop(q)

        if w > cost[r][c]:
            continue

        # 인접한 노드 탐색하면서 비용 갱신 & push
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                curr_cost = w + cave[nr][nc]
                if curr_cost < cost[nr][nc]:
                    cost[nr][nc] = curr_cost
                    heappush(q, [curr_cost, nr, nc])

    return cost[N-1][N-1]


tc = 1
while True:
    N = int(input())
    if N == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(N)]

    print(f'Problem {tc}: {dijkstra(N, cave)}')
    tc += 1