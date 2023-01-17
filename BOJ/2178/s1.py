# dfs
# 백준 tc는 다 맞음
# input.txt는 틀림 (정답: 52 | 출력: 54)

import sys
sys.stdin = open('input.txt')


def dfs(node, cnt):
    global answer

    if cnt >= answer:
        return

    n, m = node
    # 도착하면 이동 거리 확인
    if n == N - 1 and m == M - 1 and answer > cnt:
        print(f'arrive!: {cnt}')
        answer = cnt
        return

    # 방문처리
    visited[n][m] = 1

    # 4방향 중 이동 가능한 길 탐색 후 방문
    for d in dirs:
        next_n, next_m = n + d[0], m + d[1]
        if 0 <= next_n < N and 0 <= next_m < M:
            if maze[next_n][next_m] and not visited[next_n][next_m]:
                dfs((next_n, next_m), cnt + 1)


N, M = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answer = 10001
visited = [[0] * M for _ in range(N)]
dfs((0, 0), 1)
print(answer)
