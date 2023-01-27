from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(start_ripe):
    q = deque([deque(start_ripe)])
    day = -1
    while q:
        ripe = q.popleft()
        day += 1
        next_ripe = deque([])
        while ripe:
            v = ripe.popleft()
            for d in dirs:
                next_v = (v[0] + d[0], v[1] + d[1])
                if 0 <= next_v[0] < N and 0 <= next_v[1] < M and box[next_v[0]][next_v[1]] == 0:
                    next_ripe.append(next_v)
                    box[next_v[0]][next_v[1]] = 1
        if next_ripe:
            q.append(next_ripe)

    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return -1

    return day


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ripe = []
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripe.append((i, j))

answer = bfs(ripe)
print(answer)