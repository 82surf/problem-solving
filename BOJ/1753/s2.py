from math import inf
from heapq import *
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
distance = [inf] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


def dijkstra(start):
    q = [[0, start]]
    distance[start] = 0

    while q:
        dist, node = heappop(q)
        if distance[node] < dist:
            continue
        for v, w in graph[node]:
            cost = distance[node] + w
            if cost < distance[v]:
                distance[v] = cost
                heappush(q, [cost, v])


dijkstra(start)

for i in range(1, V + 1):
    print(distance[i]) if distance[i] != inf else print('INF')
