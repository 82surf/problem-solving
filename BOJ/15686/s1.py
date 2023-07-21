# 시간 초과
# M개의 치킨집 조합마다 치킨 거리의 총 합 구하는 방식의 풀이

from math import inf
from collections import deque
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집 위치 구하기
restaurant = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            restaurant.append((i, j))


# 집에서 가장 가까운 치킨집까지 거리 구하기
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def BFS(i, j, candidates):
    q = deque([(i, j, 0)])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1
    while q:
        r, c, chicken_dist = q.popleft()
        if (r, c) in candidates:
            return chicken_dist
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc, chicken_dist + 1))
    return None


# M개의 치킨집을 고르는 조합 => 각 경우의 수마다 치킨 거리의 합 구하기
answer = inf
for candidates in combinations(restaurant, M):  # M개의 치킨집을 고르는 조합
    total_chicken_dist = 0  # 치킨 거리의 총 합
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                total_chicken_dist += BFS(i, j, candidates)

    # 가장 작은 치킨 거리 구하기
    if answer > total_chicken_dist:
        answer = total_chicken_dist

print(answer)