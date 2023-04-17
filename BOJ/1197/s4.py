"""
유형: 최소 비용 신장 트리
풀이: 간선의 개수가 많아 Prim 알고리즘 사용
"""

from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def prim(start, weight):
    visited = [0] * (V + 1)
    q = [[weight, start]]
    total = 0
    cnt = 0
    while cnt < V:
        w, n = heappop(q)
        if not visited[n]:
            visited[n] = 1
            total += w
            cnt += 1
            for edge in graph[n]:
                heappush(q, edge)
    return total


V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append([w, b])
    graph[b].append([w, a])

print(prim(1, 0))