from math import inf
from collections import deque
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)


def BFS(s):
    q = deque([(s, 0)])
    visited = [0] * (N + 1)
    visited[s] = 1

    total_cnt = 0
    while q:
        v, cnt = q.popleft()
        # print(v, cnt)
        total_cnt += cnt
        for next_v in edges[v]:
            if not visited[next_v]:
                q.append((next_v, cnt + 1))
                visited[next_v] = 1
    return total_cnt


min_val = inf
answer = 0
for i in range(1, N + 1):
    k = BFS(i)
    if min_val > k:
        min_val = k
        answer = i
    elif min_val == k and answer > i:
        answer = i

print(answer)