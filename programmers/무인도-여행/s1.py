from collections import deque


def solution(maps):
    maps = list(map(list, maps))
    N, M = len(maps), len(maps[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    answer = []

    def bfs(r, c):
        visited = [[0 for _ in range(M)] for _ in range(N)]
        visited[r][c] = 1
        q = deque([(r, c)])
        foods = 0
        while q:
            curr_r, curr_c = q.popleft()
            foods += int(maps[curr_r][curr_c])
            maps[curr_r][curr_c] = 'X'
            for d in dirs:
                next_r, next_c = curr_r + d[0], curr_c + d[1]
                if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c] and maps[next_r][next_c] != 'X':
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = 1
        answer.append(foods)

    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X':
                bfs(i, j)

    return sorted(answer) if answer else [-1]