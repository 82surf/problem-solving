"""
유형: 최소 비용 신장 트리
풀이: 간선의 개수가 많아 Prim 알고리즘 사용
결과: 시간초과
"""

from heapq import heapify, heappush, heappop
import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append([w, b])
    graph[b].append([w, a])


def prim(graph, start):
    visited = [0] * (V + 1)
    visited[start] = 1

    candidate = graph[start]
    heapify(candidate)

    total = 0
    cnt = 0

    while candidate:
        c = heappop(candidate)
        w, n = c
        if not visited[n]:
            visited[n] = 1
            cnt += 1
            total += w

        for edge in graph[n]:
            if not visited[edge[1]]:
                heappush(candidate, edge)

    return total


print(prim(graph, 1))
