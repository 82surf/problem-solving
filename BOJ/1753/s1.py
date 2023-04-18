# 시간초과
# 순차탐색으로 O(V^2)

from math import inf
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
distance = [inf] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])


# 방문하지 않은 노드 중 시작노드와 최단거리인 노드 반환
def get_smallest_node():
    min_val = inf
    idx = 0
    for i in range(1, V + 1):
        if not visited[i] and min_val > distance[i]:
            min_val = distance[i]
            idx = i
    return idx


# 다익스트라
def dijkstra(start):
    # 시작 노드 거리 저장, 방문 처리
    distance[start] = 0
    visited[start] = 1

    # 시작 노드와 인접한 노드들의 distance 갱신
    for v, w in graph[start]:
        distance[v] = w

    # 시작 노드를 제외한 V-1개의 노드 처리
    for _ in range(V - 1):
        # 방문 가능한 정점 중 시작 노드와 가장 가까운 노드 방문
        curr = get_smallest_node()
        visited[curr] = True

        # 방문한 노드와 인접한 노드들의 distance 갱신
        for nxt_v, nxt_w in graph[curr]:
            cost = distance[curr] + nxt_w
            if cost < distance[nxt_v]:
                distance[nxt_v] = cost


dijkstra(start)

for i in range(1, V + 1):
    print(distance[i]) if distance[i] != inf else print('INF')
