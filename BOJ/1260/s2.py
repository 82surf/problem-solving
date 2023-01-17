from collections import deque
import sys
input = sys.stdin.readline


def dfs(v, visited):
    print(v, end=' ')
    visited[v] = 1
    for node in graph[v]:
        if not visited[node]:
            dfs(node, visited)


def bfs(s):
    visited = [0 for _ in range(N + 1)]
    visited[s] = 1
    q = deque([s])
    while q:
        v = q.popleft()
        print(v, end=' ')
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = 1


N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N + 1):
    graph[i].sort()

dfs(V, [0 for _ in range(N + 1)])
print()
bfs(V)
