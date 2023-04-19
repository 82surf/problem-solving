from math import inf
from heapq import heappush, heappop
import sys
input = sys.stdin.readline


def dijkstra(n, start, end):
    q = [(0, start)]
    cost = [inf] * (n + 1)
    cost[start] = 0

    while q:
        w, n = heappop(q)
        if w > cost[n]:
            continue

        for nxt_v, nxt_w in graph[n]:
            curr_cost = nxt_w + cost[n]
            if curr_cost < cost[nxt_v]:
                cost[nxt_v] = curr_cost
                heappush(q, (curr_cost, nxt_v))

    return cost[end]


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
start, end = map(int, input().split())
print(dijkstra(N, start, end))
