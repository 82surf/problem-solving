from collections import deque
import sys
sys.stdin = open('input.txt')


def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = 1
    cnt = 0
    while q:
        r, c = q.popleft()
        cnt += 1
        for d in dirs:
            next_r, next_c = r + d[0], c + d[1],
            if 0 <= next_r < N and 0 <= next_c < N:
                if graph[next_r][next_c] and not visited[next_r][next_c]:
                    visited[next_r][next_c] = 1
                    graph[next_r][next_c] = 0
                    q.append((next_r, next_c))
    return cnt


N = int(input())
graph = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

complex_cnt = 0
house_cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            complex_cnt += 1
            house_cnt.append(bfs((i, j)))
house_cnt.sort()

print(complex_cnt)
for c in house_cnt:
    print(c)