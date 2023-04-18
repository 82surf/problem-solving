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


# 다익스트라
def dijkstra(start):
    # 우선순위 큐에 시작 정보 삽입
    q = [[0, start]]
    # 시작 노드 거리 갱신
    distance[start] = 0

    while q:
        dist, node = heappop(q)
        # 큐에서 뽑은 노드까지 최단 거리가 최단 거리 배열의 값보다 크면 갱신 과정 생략
        if distance[node] < dist:
            continue
        # 큐에서 뽑은 노드와 인접한 노드 탐색
        for v, w in graph[node]:
            # w: 큐에서 뽑은 노드 -> 인접 노드까지 거리
            # distance[node]: 시작 -> 큐에서 뽑은 노드까지 최단거리
            # distance[v]: 시작 -> 인접 노드까지 거리
            cost = w + distance[node]
            # cost가 시작 -> 인접 노드의 거리보다 작으면
            if cost < distance[v]:
                distance[v] = cost      # 최단거리 갱신
                heappush(q, [cost, v])  # 큐에 삽입


dijkstra(start)

for i in range(1, V + 1):
    print(distance[i]) if distance[i] != inf else print('INF')
