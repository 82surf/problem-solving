# python3 시간초과
# pypy3 통과

import sys
input = sys.stdin.readline


def dfs(s):
    global answer, max_cnt

    visited = [0 for _ in range(N + 1)]
    stack = [s]
    cnt = 0
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            cnt += 1
            for node in arr[v]:
                if not visited[node]:
                    stack.append(node)

    if max_cnt < cnt:
        max_cnt = cnt
        answer = [s]
    elif max_cnt == cnt:
        answer.append(s)


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b].append(a)

max_cnt = 0
answer = []

for i in range(1, N + 1):
    dfs(i)

print(*answer)
