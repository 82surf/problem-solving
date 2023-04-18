# 다익스트라

from math import inf
from heapq import heappush, heappop


def solution(N, road, K):
    distance = [inf] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    def dijkstra(start):
        q = [[0, start]]
        distance[start] = 0

        while q:
            dist, node = heappop(q)
            if dist > distance[node]:
                continue

            # 인접 노드 탐색
            for n, w in graph[node]:
                cost = distance[node] + w
                if cost < distance[n]:
                    distance[n] = cost
                    heappush(q, [cost, n])

    dijkstra(1)

    answer = 0
    for dist in distance:
        if dist <= K:
            answer += 1

    return answer