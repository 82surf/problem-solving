# python3 시간초과
# pypy3 시간초과

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(v, visited, s):
    visited[v] = 1
    cnt[s] += 1
    for node in graph[v]:
        if not visited[node]:
            dfs(node, visited, s)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

cnt = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    dfs(i, [0 for _ in range(N + 1)], i)

max_cnt = max(cnt)
for i, c in enumerate(cnt):
    if c == max_cnt:
        print(i, end=' ')
