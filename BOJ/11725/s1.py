# 인접리스트 생성 후 BFS 순회하며 부모 노드를 기록하는 방식

from collections import deque
import sys
sys.stdin = open('input.txt')


def BFS(s):
    visited = [0 for _ in range(N + 1)]
    visited[s] = 1
    q = deque([s])
    while q:
        v = q.popleft()
        for next_v in arr[v]:
            if not visited[next_v]:
                q.append(next_v)
                visited[next_v] = 1
                answer[next_v] = v


N = int(input())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = [0 for _ in range(N + 1)]

BFS(1)

for i in range(2, N + 1):
    print(answer[i])
