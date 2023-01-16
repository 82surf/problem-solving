# 입력이 최대 10만까지 반복되므로 sys.stdin.readline 사용
# DFS로 탐색하면서 부모 노드 기록

import sys
rl = sys.stdin.readline


def DFS(s):
    answer[s] = 1
    stack = [s]
    while stack:
        v = stack.pop()
        for node in arr[v]:
            if answer[node] == 0:
                answer[node] = v
                stack.append(node)


N = int(rl())
arr = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, rl().split())
    arr[a].append(b)
    arr[b].append(a)

answer = [0 for _ in range(N + 1)]
DFS(1)
print(*answer[2:], sep='\n')