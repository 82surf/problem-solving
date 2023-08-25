import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


def DFS(s):
    visited[s] = 1
    for next in arr[s]:
        if not visited[next]:
            DFS(next)

answer = 0
for i in range(1, N + 1):
    if not visited[i]:
        answer += 1
        DFS(i)

print(answer)